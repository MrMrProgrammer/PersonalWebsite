from django.db import models


# Create your models here.

class HomeData(models.Model):
    page_title = models.CharField(max_length=100)
    page_header = models.CharField(max_length=100)
    Skills = models.CharField(max_length=100)
    help_to = models.CharField(max_length=100)
    help_to_content = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='home_profile')
    about_me_header = models.CharField(max_length=200)
    about_me_content = models.CharField(max_length=500)
    instagram_link = models.CharField(max_length=200)
    linkedin_link = models.CharField(max_length=200)
    github_link = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.page_title

    class Meta:
        db_table = 'HomeData'

class ResumeProfessionalSkills(models.Model):
    skill = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.skill

    class Meta:
        db_table = 'Resume Professional Skills'


class ResumeLanguages(models.Model):
    language = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.language

    class Meta:
        db_table = 'Resume Languages'

class ResumeExperience(models.Model):
    from_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)
    is_present = models.BooleanField(default=False)
    job_title = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    content = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.job_title

    class Meta:
        db_table = 'Resume Experience'



















