# Generated by Django 4.2.3 on 2023-09-04 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='shor_name',
            field=models.CharField(max_length=20, verbose_name='Abreviacion'),
        ),
    ]