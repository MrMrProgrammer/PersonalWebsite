from django.db import models


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