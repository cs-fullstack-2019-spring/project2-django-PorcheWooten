# Generated by Django 2.0.6 on 2019-03-12 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='postSuject',
            new_name='postSubject',
        ),
        migrations.RenameField(
            model_name='relateditems',
            old_name='postSuject',
            new_name='postSubject',
        ),
    ]
