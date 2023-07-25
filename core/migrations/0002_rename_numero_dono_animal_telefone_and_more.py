# Generated by Django 4.2.3 on 2023-07-25 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='numero_dono',
            new_name='telefone',
        ),
        migrations.AlterField(
            model_name='animal',
            name='especie',
            field=models.CharField(choices=[('Cachorro ', 'Cachorro'), ('Gato ', 'Gato'), ('Passaro ', 'Passaro'), ('Cavalo ', 'Cavalo')], default='Cachorro ', max_length=15),
        ),
    ]