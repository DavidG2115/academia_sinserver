# Generated by Django 4.2.1 on 2023-05-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0004_rename_project_tema_curso_rename_titulo_tema_unidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='aprenderas2',
            field=models.TextField(null=True),
        ),
    ]
