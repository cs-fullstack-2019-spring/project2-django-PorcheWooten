# Generated by Django 2.0.6 on 2019-03-15 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0009_auto_20190315_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='postForeignKey',
            new_name='foreignKeyToPost',
        ),
    ]
