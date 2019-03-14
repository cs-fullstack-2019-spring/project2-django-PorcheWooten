# Generated by Django 2.0.6 on 2019-03-14 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WikiApp', '0005_relateditemsmodel_relateditemforeignkey'),
    ]

    operations = [
        migrations.CreateModel(
            name='WikiUserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password1', models.CharField(max_length=10)),
                ('password2', models.CharField(max_length=10)),
                ('userForeignKey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]