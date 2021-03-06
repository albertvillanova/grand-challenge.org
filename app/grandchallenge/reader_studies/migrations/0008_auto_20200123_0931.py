# Generated by Django 2.2.9 on 2020-01-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reader_studies", "0007_auto_20200121_1554"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="score",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="scoring_function",
            field=models.CharField(
                choices=[("ACC", "Accuracy score")],
                default="ACC",
                max_length=3,
            ),
        ),
    ]
