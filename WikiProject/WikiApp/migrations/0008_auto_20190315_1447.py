# Generated by Django 2.0.6 on 2019-03-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0007_auto_20190314_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='imageURL',
        ),
        migrations.RemoveField(
            model_name='relateditemsmodel',
            name='imageURL',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='wiki_post_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='relateditemsmodel',
            name='wiki_post_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]