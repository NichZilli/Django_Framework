# Generated by Django 3.2.8 on 2021-10-18 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('email', models.CharField(max_length=100, verbose_name='E-mail')),
            ],
        ),
    ]