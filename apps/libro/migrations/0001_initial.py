# Generated by Django 3.1.3 on 2021-01-09 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=220)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de publicación')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado Activo/Inactivo')),
                ('autor_id', models.ManyToManyField(to='libro.Autor')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['titulo'],
            },
        ),
    ]
