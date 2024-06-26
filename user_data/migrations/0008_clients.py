# Generated by Django 5.0 on 2023-12-23 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_data", "0007_user_company_alter_company_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Clients",
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
                ("name", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_data.company",
                    ),
                ),
            ],
        ),
    ]
