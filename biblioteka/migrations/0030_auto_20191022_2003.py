# Generated by Django 2.2.6 on 2019-10-22 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka', '0029_auto_20191022_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='wydanie',
            new_name='rok_wydania',
        ),
    ]
