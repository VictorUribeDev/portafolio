# Generated by Django 5.1.4 on 2025-01-11 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_proyecto_icono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='icono',
            field=models.CharField(blank=True, help_text='fa-brands fa-html5, fa-brands fa-bootstrap, fa-brands fa-js, fa-brands fa-python, fa-solid fa-database, fa-brands fa-python, fa-solid fa-gamepad', max_length=50, null=True),
        ),
    ]
