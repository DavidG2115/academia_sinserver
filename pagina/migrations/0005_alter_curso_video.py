# Generated by Django 4.2.1 on 2023-06-01 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0004_curso_duracion_curso_fechaarranque_curso_modalidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='video',
            field=models.TextField(null=True),
        ),
    ]
