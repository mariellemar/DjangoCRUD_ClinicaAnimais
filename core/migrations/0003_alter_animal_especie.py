# Generated by Django 4.2.3 on 2023-07-25 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_numero_dono_animal_telefone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='especie',
            field=models.CharField(choices=[('Cachorro ', 'Cachorro'), ('Gato ', 'Gato'), ('Passaro ', 'Passaro'), ('Cavalo ', 'Cavalo')], max_length=15),
        ),
    ]
