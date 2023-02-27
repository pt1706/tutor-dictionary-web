# Generated by Django 4.1.4 on 2022-12-23 07:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='correct_answers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='card',
            name='status',
            field=models.CharField(choices=[('active', 'Учить'), ('done', 'Выучено'), ('disable', 'Отложено')], default='active', max_length=10),
        ),
        migrations.AddField(
            model_name='lesson',
            name='required_answers',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
