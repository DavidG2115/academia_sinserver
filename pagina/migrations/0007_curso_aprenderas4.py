# Generated by Django 4.2.1 on 2023-05-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0006_curso_aprenderas3'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='aprenderas4',
            field=models.TextField(blank=True),
        ),
    ]
