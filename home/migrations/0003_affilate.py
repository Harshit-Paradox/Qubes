# Generated by Django 5.1 on 2024-08-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_contact_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Affilate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("number", models.CharField(max_length=15)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
