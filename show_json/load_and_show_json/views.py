import inspect
import json

from django.apps import apps
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import FullModuleInfo, Module


def load_json():
    path_to_json = "./load_json.json"
    with open(path_to_json, "r", encoding="utf-8") as file:
        data = json.load(file)
        sorted_data = {
            "module": data["module"],
            "function": data["function"],
            "data": dict(sorted(data["data"].items(), key=lambda x: tuple(map(int, x[1]["ident"].split("."))))),
        }
        module_instance = Module.objects.create(
            module=sorted_data["module"],
            function=sorted_data["function"],
        )
        for error, error_data in sorted_data["data"].items():
            if "value" in error_data:
                value = error_data["value"]
                values_array = [v.strip() for v in value.split(" ") if v.strip()]
                error_data["value"] = values_array
            FullModuleInfo.objects.create(
                module=module_instance, description=error, version=error_data["ident"], value=error_data["value"]
            )
        return sorted_data


def get_module_data(module_instances):
    result_list = []
    for module_instance in module_instances:
        data = {
            "module": module_instance.module,
            "function": module_instance.function,
            "data": list(module_instance.full.values()),
        }
        result_list.append(data)
    return result_list


@csrf_exempt
def load_data(request):
    if request.method == "POST":
        data = load_json()
        return JsonResponse(data)

    module_name = request.GET.get("module", "")
    function_name = request.GET.get("function", "")

    result_list = []

    if module_name:
        modules = Module.objects.filter(module=module_name)
        if modules:
            result_list = get_module_data(modules)
        else:
            return JsonResponse({"error": f"Unknown module {module_name}", "status": "error"}, status=500)
    elif function_name:
        functions = Module.objects.filter(function=function_name)
        if functions:
            result_list = get_module_data(functions)
        else:
            return JsonResponse({"error": f"Unknown function {function_name}", "status": "error"}, status=500)

    if result_list:
        return JsonResponse(result_list, safe=False)
    else:
        return render(request, "load_and_show_json/json.html")


def show_func(request):
    modules_with_info = Module.objects.prefetch_related("full").all()
    context = {"modules": modules_with_info}
    # print(context['modules'].query)
    return render(request, "load_and_show_json/full_info.html", context)


def get_functions_info(app_name):
    app = apps.get_app_config(app_name)
    functions_info = []

    for model in app.get_models():
        for name, func in inspect.getmembers(model, inspect.isfunction):
            docstring = inspect.getdoc(func)
            source_code = inspect.getsource(func)

            function_info = {
                "module": model.__name__,
                "function": name,
                "docstring": docstring,
                "source_code": source_code,
            }

            functions_info.append(function_info)

    return functions_info


def html_view(request):
    app_name = "load_and_show_json"
    functions_info = get_functions_info(app_name)

    context = {"functions_info": functions_info}

    return render(request, "load_and_show_json/info_my_module.html", context)
