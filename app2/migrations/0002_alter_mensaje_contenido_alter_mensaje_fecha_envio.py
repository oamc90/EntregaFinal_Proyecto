# Generated by Django 4.0.4 on 2022-06-07 11:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='contenido',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='fecha_envio',
            field=models.TextField(default='dd/mm/aa'),
        ),
    ]
