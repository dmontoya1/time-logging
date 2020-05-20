# Generated by Django 3.0.5 on 2020-05-20 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        ('configuration', '0001_initial'),
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('initial_time', models.TimeField(verbose_name='Hora de inicio')),
                ('end_time', models.TimeField(verbose_name='Hora de finalización')),
                ('place', models.CharField(choices=[('IL', 'Ilana'), ('VT', 'VeriTran'), ('TT', 'TeleTrabajo')], default='TT', max_length=2, verbose_name='Lugar de ejecución')),
                ('description', models.TextField(verbose_name='Descripción de la actividad')),
                ('activity', models.TextField(verbose_name='Flujo o actividad')),
                ('action', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loggers', to='configuration.Action', verbose_name='Acción que se realiza')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Category', verbose_name='Categoría')),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='configuration.Device', verbose_name='Dispositivo')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loggers', to='project.Project', verbose_name='Proyecto')),
                ('project_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.ProjectType', verbose_name='Tipo de proyecto')),
                ('responsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loggers', to=settings.AUTH_USER_MODEL, verbose_name='Responsable')),
                ('sub_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.SubProject', verbose_name='Sub Proyecto')),
            ],
            options={
                'verbose_name': 'Registro',
            },
        ),
    ]