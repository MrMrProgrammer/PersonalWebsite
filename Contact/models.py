from django.db import models
from django_jalali.db import models as jmodels


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    message = models.TextField()
    datetime = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'Contact'