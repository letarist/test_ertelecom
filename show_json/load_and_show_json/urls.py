from django.urls import path

from .views import html_view, load_data, show_func

app_name = "json"
urlpatterns = [path("json/", load_data), path("html/", show_func), path("my_func/", html_view)]
