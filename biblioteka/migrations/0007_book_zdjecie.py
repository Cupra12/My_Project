# Generated by Django 2.2.6 on 2019-10-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka', '0006_auto_20191012_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='zdjecie',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
