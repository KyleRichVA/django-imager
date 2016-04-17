from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from django.conf import settings
from imager_profile.models import User_Profile
import logging
logger = logging.getLogger(__name__)


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
