# Generated by Django 2.2.6 on 2019-10-12 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ksiazka',
            old_name='opis',
            new_name='gatunek',
        ),
    ]
