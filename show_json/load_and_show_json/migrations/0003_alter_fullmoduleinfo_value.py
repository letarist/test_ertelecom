# Generated by Django 4.2 on 2023-11-12 19:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "load_and_show_json",
            "0002_rename_model_module_module_remove_module_data_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="fullmoduleinfo",
            name="value",
            field=models.JSONField(max_length=1000, verbose_name="Массив"),
        ),
    ]