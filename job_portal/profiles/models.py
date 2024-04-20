# profiles/models.py
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    contact_details = models.CharField(max_length=100)
    skills = models.TextField()
    extracurricular_activities = models.TextField()
    education = models.TextField()
    other_information = models.TextField()