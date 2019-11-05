# Generated by Django 2.2.6 on 2019-10-13 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka', '0011_auto_20191012_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='opis',
            field=models.CharField(default=22, max_length=224),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='autor',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='zdjecie',
            field=models.ImageField(null=True, upload_to='Pictures'),
        ),
    ]
