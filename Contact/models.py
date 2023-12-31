from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'Contact'
