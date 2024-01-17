from django.db import models


class Logger(models.Model):
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    ip = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    language = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Log'
        verbose_name = "Log"
        verbose_name_plural = "Logs"
