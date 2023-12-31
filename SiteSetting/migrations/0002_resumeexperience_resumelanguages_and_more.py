# Generated by Django 4.2.7 on 2023-11-09 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteSetting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('is_present', models.BooleanField(default=False)),
                ('job_title', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Resume Experience',
            },
        ),
        migrations.CreateModel(
            name='ResumeLanguages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Resume Languages',
            },
        ),
        migrations.CreateModel(
            name='ResumeProfessionalSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Resume Professional Skills',
            },
        ),
    ]
