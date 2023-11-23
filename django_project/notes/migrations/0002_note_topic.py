# Generated by Django 4.2.7 on 2023-11-18 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("topics", "0004_topic_created_by_alter_topic_public"),
        ("notes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="topic",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="note_topic",
                to="topics.topic",
            ),
        ),
    ]
