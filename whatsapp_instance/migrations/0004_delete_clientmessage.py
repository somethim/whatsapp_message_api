# Generated by Django 5.0 on 2023-12-23 17:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("whatsapp_instance", "0003_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ClientMessage",
        ),
    ]