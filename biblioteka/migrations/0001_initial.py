# Generated by Django 2.2.6 on 2019-10-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ksiazka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.TextField()),
                ('opis', models.TextField()),
                ('cena', models.TextField()),
                ('wydanie', models.TextField()),
                ('autor', models.TextField()),
            ],
        ),
    ]