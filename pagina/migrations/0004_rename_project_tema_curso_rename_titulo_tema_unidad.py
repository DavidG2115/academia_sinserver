# Generated by Django 4.2.1 on 2023-05-28 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0003_rename_descripciondentrp_curso_descripciondentro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tema',
            old_name='project',
            new_name='curso',
        ),
        migrations.RenameField(
            model_name='tema',
            old_name='titulo',
            new_name='unidad',
        ),
    ]