from django.db import models

class WorkExperience(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)
    employer = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    date_started = models.DateField()
    date_left = models.DateField()

    def __str__(self):
        return f'{self.title} - {self.employer}'

class Education(models.Model):
    pass

class Publication(models.Model):
    pass
