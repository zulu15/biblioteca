# Generated by Django 3.1.3 on 2021-02-13 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_auto_20210205_2323'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'permissions': [('ver_recetas', 'Puede ver las recetas de los pacientes'), ('editar_recetas', 'Puede editar recetas de los pacientes')]},
        ),
    ]
