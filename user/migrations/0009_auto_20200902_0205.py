# Generated by Django 3.1 on 2020-09-01 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20200902_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='outTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 2, 2, 35, 12, 709328)),
        ),
    ]
