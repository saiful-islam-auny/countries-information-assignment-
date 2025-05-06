from django.db import models

# -------------------------------
# Language Model
# -------------------------------
class Language(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# -------------------------------
# Country Model
# -------------------------------
class Country(models.Model):
    name = models.CharField(max_length=100, db_index=True)  # Indexed for fast search by name
    cca2 = models.CharField(max_length=2, unique=True, db_index=True) 
    capital = models.CharField(max_length=100, blank=True, null=True) 
    population = models.BigIntegerField()
    region = models.CharField(max_length=100, db_index=True)
    timezones = models.JSONField()
    flag = models.URLField()
    languages = models.ManyToManyField(Language)  # each country can have multiple languages

    def __str__(self):
        return self.name  # Display name in admin or shell