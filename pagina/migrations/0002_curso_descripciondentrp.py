# Generated by Django 4.2.1 on 2023-05-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='descripcionDentrp',
            field=models.TextField(null=True),
        ),
    ]