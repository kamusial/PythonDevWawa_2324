# Generated by Django 5.0.2 on 2024-02-18 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("flashcards_app", "0003_flashcard_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="flashcard",
            name="image",
        ),
    ]
