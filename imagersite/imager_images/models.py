from __future__ import unicode_literals

from django.db import models
from imager_profile.models import User_Profile

# Create your models here.


class Album(models.Model):
    pass


class Photo(models.Model):
    file = models.FilePathField(path='/images')
    owner = models.ForeignKey(User_Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    date_uploaded = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    date_published = models.DateField()
    PUBLISH_CHOICES = (
        ('PRIV', 'Private'),
        ('SHARE', 'Shared'),
        ('PUBLIC', 'Public'),
    )
    published = models.CharField(max_length=6,
                                 choices=PUBLISH_CHOICES,
                                 default='PUBLIC')
