# Generated by Django 2.2.6 on 2019-10-20 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka', '0016_auto_20191020_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='ocena',
            field=models.IntegerField(choices=[(3, 'Dobra'), (0, 'Nieznany'), (4, 'Bardzo dobra'), (2, 'Średnia'), (1, 'Słaba'), (5, 'Arcydzieło')], default=0),
        ),
    ]
