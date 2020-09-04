# Generated by Django 3.0.9 on 2020-08-24 11:10

import django.db.models.deletion
import django_extensions.db.fields
import simple_history.models
from django.conf import settings
from django.db import migrations, models

import grandchallenge.challenges.models
import grandchallenge.core.storage


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=1024)),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        max_length=1024,
                        populate_from="title",
                    ),
                ),
                ("description", models.TextField()),
                ("content", models.TextField()),
                (
                    "logo",
                    models.ImageField(
                        storage=grandchallenge.core.storage.PublicS3Storage(),
                        upload_to=grandchallenge.challenges.models.get_logo_path,
                    ),
                ),
                ("published", models.BooleanField(default=False)),
                (
                    "authors",
                    models.ManyToManyField(to=settings.AUTH_USER_MODEL),
                ),
            ],
            options={"ordering": ("-created",)},
        ),
        migrations.CreateModel(
            name="HistoricalPost",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        auto_created=True,
                        blank=True,
                        db_index=True,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(blank=True, editable=False)),
                ("modified", models.DateTimeField(blank=True, editable=False)),
                ("title", models.CharField(max_length=1024)),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        max_length=1024,
                        populate_from="title",
                    ),
                ),
                ("description", models.TextField()),
                ("content", models.TextField()),
                ("logo", models.TextField(max_length=100)),
                ("published", models.BooleanField(default=False)),
                (
                    "history_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("history_date", models.DateTimeField()),
                (
                    "history_change_reason",
                    models.CharField(max_length=100, null=True),
                ),
                (
                    "history_type",
                    models.CharField(
                        choices=[
                            ("+", "Created"),
                            ("~", "Changed"),
                            ("-", "Deleted"),
                        ],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical post",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
