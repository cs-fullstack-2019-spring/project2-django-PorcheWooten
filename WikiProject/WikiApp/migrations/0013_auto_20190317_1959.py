# Generated by Django 2.0.6 on 2019-03-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0012_wikiusermodel_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relateditemsmodel',
            name='relatedItemForeignKey',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='relatedPostSubject',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='relatedpostText',
            field=models.TextField(blank=True, default='', max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='relatedwiki_post_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/'),
        ),
        migrations.DeleteModel(
            name='RelatedItemsModel',
        ),
    ]
