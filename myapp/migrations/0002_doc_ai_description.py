# Generated by Django 5.2.1 on 2025-05-25 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="doc",
            name="AI_description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
