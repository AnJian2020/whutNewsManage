# Generated by Django 3.1 on 2020-09-11 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manuscript', '0005_auto_20200908_1150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkmanuscriptmodel',
            old_name='id',
            new_name='check_id',
        ),
        migrations.RenameField(
            model_name='reviewmanuscriptmodel',
            old_name='id',
            new_name='review_id',
        ),
    ]