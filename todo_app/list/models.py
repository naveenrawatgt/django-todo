from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=30)
    details = models.CharField(max_length=90)
    status = models.BooleanField()

    def __str__(self) -> str:
        return self.title