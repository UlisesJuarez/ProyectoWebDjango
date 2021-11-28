# Generated by Django 3.0.5 on 2021-11-24 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='Url amigable')),
                ('visible', models.BooleanField(verbose_name='¿Visible?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Página',
                'verbose_name_plural': 'Páginas',
            },
        ),
    ]
