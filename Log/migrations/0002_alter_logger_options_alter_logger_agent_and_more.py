# Generated by Django 4.2.7 on 2024-01-17 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logger',
            options={'verbose_name': 'Log', 'verbose_name_plural': 'Logs'},
        ),
        migrations.AlterField(
            model_name='logger',
            name='agent',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='logger',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='logger',
            name='ip',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='logger',
            name='language',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='logger',
            name='time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterModelTable(
            name='logger',
            table='Log',
        ),
    ]