from django.db import models

class WorkExperience(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)
    employer = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    date_started = models.DateField()
    date_left = models.DateField(blank=True, null=True)
    current_employer = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} - {self.employer}'

class Education(models.Model):
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    minor = models.CharField(max_length=255, blank=True, null=True)
    gpa = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    date_started = models.DateField()
    graduation_date = models.DateField()

    def __str__(self):
        return f'{self.school} - {self.degree}'


class Publication(models.Model):
    title = models.CharField(max_length=510)
    abstract = models.TextField(max_length=5000)
    journal = models.CharField(max_length=510)
    year = models.CharField(max_length=255)
    number_of_authors = models.IntegerField()
    authors = models.CharField(max_length=510)
    feature_image = models.ImageField(upload_to='publication_pics', blank=True, null=True)
    doi = models.CharField(max_length=255, blank=True, null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'
