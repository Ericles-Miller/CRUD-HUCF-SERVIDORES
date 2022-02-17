# Generated by Django 4.0 on 2021-12-30 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='Cpf')),
                ('imagem', models.ImageField(upload_to='imagens/', verbose_name='Imagem Crachá')),
            ],
        ),
    ]