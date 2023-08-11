# Generated by Django 4.2.3 on 2023-08-09 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="postmodel",
            name="publish",
            field=models.CharField(
                choices=[
                    ("draft", "Draft"),
                    ("publish", "Publish"),
                    ("private", "Private"),
                ],
                default="draft",
                max_length=120,
            ),
        ),
        migrations.AlterField(
            model_name="postmodel",
            name="content",
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]