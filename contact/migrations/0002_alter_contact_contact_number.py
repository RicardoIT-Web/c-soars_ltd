# Generated by Django 3.2 on 2022-07-14 15:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+9999999999'.                 Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
