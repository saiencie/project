from django.db import models

class Log(models.Model):
    ip_address = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=100)
    request = models.TextField()
    status_code = models.IntegerField()
    response_size = models.IntegerField()
    user_agent = models.TextField()

    def __str__(self):
        return f"{self.ip_address} - {self.timestamp} - {self.status_code}"
