# Generated by Django 4.2.8 on 2023-12-21 11:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dinnerApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="categories",
            field=models.ManyToManyField(related_name="items", to="dinnerApp.category"),
        ),
    ]
