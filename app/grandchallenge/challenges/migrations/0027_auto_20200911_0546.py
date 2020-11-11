# Generated by Django 3.0.9 on 2020-09-11 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("forum", "0011_auto_20190627_2132"),
        ("challenges", "0026_auto_20200908_1139"),
    ]

    operations = [
        migrations.AlterField(
            model_name="challenge",
            name="forum",
            field=models.OneToOneField(
                editable=False,
                on_delete=django.db.models.deletion.CASCADE,
                to="forum.Forum",
            ),
        ),
        migrations.AddField(
            model_name="challenge",
            name="display_forum_link",
            field=models.BooleanField(
                default=False,
                help_text="Display a link to the challenge forum in the nav bar.",
            ),
        ),
    ]