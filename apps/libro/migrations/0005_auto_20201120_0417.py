# Generated by Django 3.1.3 on 2020-11-20 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0004_auto_20201120_0414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='autor_id',
        ),
        migrations.AddField(
            model_name='libro',
            name='autor_id',
            field=models.ManyToManyField(to='libro.Autor'),
        ),
    ]