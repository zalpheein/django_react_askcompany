# Generated by Django 3.2 on 2021-11-30 14:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_auto_20211115_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
