# Generated by Django 2.0.6 on 2019-03-17 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0014_auto_20190317_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relateditemsmodel',
            old_name='postSubject',
            new_name='relatedpostSubject',
        ),
        migrations.RenameField(
            model_name='relateditemsmodel',
            old_name='postText',
            new_name='relatedpostText',
        ),
        migrations.RenameField(
            model_name='relateditemsmodel',
            old_name='wiki_post_image',
            new_name='relatedwiki_post_image',
        ),
    ]