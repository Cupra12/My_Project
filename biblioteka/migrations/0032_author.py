# Generated by Django 2.2.6 on 2019-11-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka', '0031_auto_20191023_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie_nazwisko', models.CharField(max_length=60)),
                ('urodzony', models.IntegerField(blank=True, null=True)),
                ('data_smierci', models.IntegerField(blank=True, null=True)),
                ('zdjecie_autora', models.ImageField(null=True, upload_to='')),
                ('informacje', models.TextField()),
            ],
        ),
    ]
