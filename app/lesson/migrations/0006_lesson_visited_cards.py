# Generated by Django 4.1.4 on 2022-12-30 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0005_remove_card_attempts'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='visited_cards',
            field=models.ManyToManyField(related_name='visited_cards', to='lesson.card'),
        ),
    ]
