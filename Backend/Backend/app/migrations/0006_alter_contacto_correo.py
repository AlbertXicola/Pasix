# Generated by Django 4.1.13 on 2023-12-18 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_contactos_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='correo',
            field=models.EmailField(max_length=254),
        ),
    ]
