# Generated by Django 4.2.7 on 2023-11-17 22:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("topics", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="topic",
            name="public_field",
            field=models.BooleanField(default=1, verbose_name=False),
            preserve_default=False,
        ),
    ]
