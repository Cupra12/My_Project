# Generated by Django 2.2.6 on 2019-10-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka', '0019_auto_20191020_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='ocena',
            field=models.IntegerField(choices=[(2, 'Średnia'), (4, 'Bardzo dobra'), (0, 'Nieznany'), (5, 'Arcydzieło'), (3, 'Dobra'), (1, 'Słaba')], default=0),
        ),
    ]
