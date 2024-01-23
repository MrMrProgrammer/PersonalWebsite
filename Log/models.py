from django.db import models


class Logger(models.Model):
    ip = models.CharField(max_length=20)
    count = models.IntegerField(default=1)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    agent = models.CharField(max_length=500)
    language = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Log'
        verbose_name = "Log"
        verbose_name_plural = "Logs"
