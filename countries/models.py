from django.db import models

class Language(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    cca2 = models.CharField(max_length=2, unique=True)
    capital = models.CharField(max_length=100, blank=True, null=True)
    population = models.BigIntegerField()
    region = models.CharField(max_length=100)
    timezones = models.JSONField()
    flag = models.URLField()
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
