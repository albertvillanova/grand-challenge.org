# Generated by Django 3.1.1 on 2020-10-01 07:58

from django.db import migrations, models

import grandchallenge.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ("evaluation", "0006_auto_20200925_1516"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evaluation",
            name="rank_per_metric",
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="phase",
            name="extra_results_columns",
            field=models.JSONField(
                blank=True,
                default=list,
                help_text="A JSON object that contains the extra columns from metrics.json that will be displayed on the results page. ",
                validators=[
                    grandchallenge.core.validators.JSONSchemaValidator(
                        schema={
                            "$schema": "http://json-schema.org/draft-06/schema#",
                            "definitions": {},
                            "items": {
                                "$id": "#/items",
                                "additionalProperties": False,
                                "properties": {
                                    "error_path": {
                                        "$id": "#/items/properties/error_path",
                                        "default": "",
                                        "examples": ["aggregates.dice.std"],
                                        "pattern": "^(.*)$",
                                        "title": "The Error Path Schema",
                                        "type": "string",
                                    },
                                    "order": {
                                        "$id": "#/items/properties/order",
                                        "default": "",
                                        "enum": ["asc", "desc"],
                                        "examples": ["asc"],
                                        "pattern": "^(asc|desc)$",
                                        "title": "The Order Schema",
                                        "type": "string",
                                    },
                                    "path": {
                                        "$id": "#/items/properties/path",
                                        "default": "",
                                        "examples": ["aggregates.dice.mean"],
                                        "pattern": "^(.*)$",
                                        "title": "The Path Schema",
                                        "type": "string",
                                    },
                                    "title": {
                                        "$id": "#/items/properties/title",
                                        "default": "",
                                        "examples": ["Mean Dice"],
                                        "pattern": "^(.*)$",
                                        "title": "The Title Schema",
                                        "type": "string",
                                    },
                                },
                                "required": ["title", "path", "order"],
                                "title": "The Items Schema",
                                "type": "object",
                            },
                            "title": "The Extra Results Columns Schema",
                            "type": "array",
                        }
                    )
                ],
            ),
        ),
    ]
