from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    project_image = models.ImageField(upload_to='Project')
    link = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name

    class Meta:
        db_table = 'Project'
