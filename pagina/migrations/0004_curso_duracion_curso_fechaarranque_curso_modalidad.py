# Generated by Django 4.2.1 on 2023-06-01 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0003_remove_curso_dirigido_a_2_remove_curso_dirigido_a_3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='duracion',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='fechaArranque',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='modalidad',
            field=models.TextField(null=True),
        ),
    ]