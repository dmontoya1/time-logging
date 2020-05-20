# Generated by Django 3.0.5 on 2020-05-20 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nmobre')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='category.Category', verbose_name='Categoría Padre')),
            ],
            options={
                'verbose_name': 'Categoría',
                'ordering': ['name'],
            },
        ),
    ]