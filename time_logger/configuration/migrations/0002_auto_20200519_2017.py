# Generated by Django 3.0.5 on 2020-05-20 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'ordering': ['name'], 'verbose_name': 'Dispositivo'},
        ),
    ]
