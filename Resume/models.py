from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    priority = models.IntegerField(
        default=5,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        blank=True, null=True,
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.skill_name

    class Meta:
        db_table = 'Skill'


class Language(models.Model):
    language = models.CharField(max_length=100)
    priority = models.IntegerField(
        default=5,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        blank=True, null=True,
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.language

    class Meta:
        db_table = 'Language'


class Experience(models.Model):
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
        db_table = 'Experience'
