# Generated by Django 4.2.7 on 2024-01-23 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0003_logger_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='logger',
            name='client_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
