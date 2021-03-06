# Generated by Django 3.0.10 on 2020-09-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0005_auto_20200904_1015"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="creators_ip",
            field=models.GenericIPAddressField(
                default=None, editable=False, null=True
            ),
        ),
        migrations.AddField(
            model_name="submission",
            name="creators_user_agent",
            field=models.TextField(blank=True, default="", editable=False),
        ),
    ]
