# Generated by Django 4.2.7 on 2023-11-18 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SiteSetting', '0002_resumeexperience_resumelanguages_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ResumeExperience',
        ),
        migrations.DeleteModel(
            name='ResumeLanguages',
        ),
        migrations.DeleteModel(
            name='ResumeProfessionalSkills',
        ),
    ]
