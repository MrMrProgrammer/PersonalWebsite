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