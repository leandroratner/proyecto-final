# Generated by Django 4.1.3 on 2022-12-09 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0004_mvpfamiliares'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mvpfamiliares',
            old_name='direccion',
            new_name='edad',
        ),
        migrations.RenameField(
            model_name='mvpfamiliares',
            old_name='localidad',
            new_name='fecha_de_nacimiento',
        ),
        migrations.RenameField(
            model_name='mvpfamiliares',
            old_name='trabajo',
            new_name='ultimo_trabajo',
        ),
    ]
