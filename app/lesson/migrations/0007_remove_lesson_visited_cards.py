# Generated by Django 4.1.4 on 2022-12-30 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0006_lesson_visited_cards'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='visited_cards',
        ),
    ]
