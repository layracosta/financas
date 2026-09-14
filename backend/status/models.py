from django.db import models

class Status(models.Model):

    status = models.CharField(max_length=200)

    def __str__(self):
        return f"({self.status})"