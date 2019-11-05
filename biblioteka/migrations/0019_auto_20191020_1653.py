# Generated by Django 2.2.6 on 2019-10-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka', '0018_auto_20191020_1652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extrainfo',
            old_name='czas_trwania',
            new_name='ilosc_stron',
        ),
        migrations.RemoveField(
            model_name='extrainfo',
            name='rodzaj',
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='ocena',
            field=models.IntegerField(choices=[(2, 'Średnia'), (1, 'Słaba'), (5, 'Arcydzieło'), (3, 'Dobra'), (4, 'Bardzo dobra'), (0, 'Nieznany')], default=0),
        ),
    ]
