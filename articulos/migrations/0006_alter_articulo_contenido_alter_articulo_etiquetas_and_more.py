# Generated by Django 5.1.3 on 2024-11-25 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0005_alter_articulo_options_alter_articulo_etiquetas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='contenido',
            field=models.TextField(help_text='Escribe el contenido completo del artículo aquí.', verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='etiquetas',
            field=models.CharField(blank=True, help_text='Etiquetas separadas por comas, ej: reflexión, conciencia.', max_length=200, null=True, verbose_name='Etiquetas'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='titulo',
            field=models.CharField(help_text='Introduce un título descriptivo para el artículo (máximo 200 caracteres).', max_length=200, verbose_name='Título'),
        ),
    ]
