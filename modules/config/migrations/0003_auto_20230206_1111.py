# Generated by Django 3.2.9 on 2023-02-06 11:11
import os

from django.db import migrations


def create_default_config(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Config = apps.get_model("config", "Config")
    login_path = os.getenv("LOGIN_PATH")
    save_message_seven_days = os.getenv("SAVE_MESSAGE_SEVEN_DAYS")
    register_type = os.getenv("REGISTER_TYPE")

    Config.objects.bulk_create(
        [
            Config(name="LOGIN_PATH", type=0, value=login_path),
            Config(name="SAVE_MESSAGE_SEVEN_DAYS", type=0, value=save_message_seven_days),
            Config(name="REGISTER_TYPE", type=0, value=register_type),
        ]
    )

    Config.objects.filter(name="SERVER_IP").update(type=0)


class Migration(migrations.Migration):
    dependencies = [
        ('config', '0002_auto_20220826_0751'),
    ]
    operations = [
        migrations.RunPython(create_default_config),
    ]
