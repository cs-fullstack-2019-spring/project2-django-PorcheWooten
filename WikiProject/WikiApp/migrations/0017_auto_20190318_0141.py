# Generated by Django 2.0.6 on 2019-03-18 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0016_auto_20190318_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='postSubject',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='postText',
            field=models.TextField(blank=True, default='', max_length=2000, null=True),
        ),
    ]