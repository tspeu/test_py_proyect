# Generated by Django 3.1.2 on 2020-10-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='f_creado',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='f_entregado',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='f_final',
            field=models.DateField(auto_now=True),
        ),
    ]
