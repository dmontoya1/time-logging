# Generated by Django 3.0.5 on 2020-05-20 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Código o abbr')),
            ],
            options={
                'verbose_name': 'Proyecto',
            },
        ),
        migrations.CreateModel(
            name='SubProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'SubProyecto',
            },
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Project', verbose_name='Proyecto')),
                ('sub_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.SubProject', verbose_name='Subproyecto')),
            ],
            options={
                'verbose_name': 'Tipo de Proyecto',
                'verbose_name_plural': 'Tipos de Proyecto',
            },
        ),
    ]
