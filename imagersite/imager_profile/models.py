from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class User_Manager(models.Manager):
    def get_queryset(self):
        return super(User_Manager, self).get_queryset().filter(
            user__is_active=True)


class User_Profile(models.Model):
    camera_model = models.CharField(max_length=300)
    photo_type = models.CharField(max_length=250)
    friends = models.ManyToManyField("self")
    region = models.CharField(max_length=250)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')

    objects = models.Manager()
    active = User_Manager()

    @property
    def is_active(self):
        return self.user.is_active
