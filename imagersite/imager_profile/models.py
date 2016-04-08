from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
import logging
logger = logging.getLogger(__name__)


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
                                related_name='profile')
    active = User_Manager()

    @property
    def is_active(self):
        return self.user.is_active


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, created, instance, **kwargs):
    if created:
        try:
            profile = User_Profile(user=instance)
            profile.save()
        except ValueError:
            msg = u'Unable to create User Profile for {}'.format(instance)
            logger.error(msg)


@receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
def remove_profile(sender, instance, **kwargs):
    try:
        instance.profile.delete()
    except AttributeError:
        msg = u"Could not delete {}. Maybe it doesn't exist?".format(instance)
        logger.warn(msg)
