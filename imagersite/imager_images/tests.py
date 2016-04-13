from django.test import TestCase, override_settings
from django.contrib.auth.models import User
from .models import Photo
from imagersite.settings import BASE_DIR
import factory
import datetime
import os

# Create your tests here.


class PhotoTestCase(TestCase):

    @override_settings(MEDIA_ROOT=os.path.join(BASE_DIR, 'test_media'))
    def setUp(self):
        self.user = UserFactory.create()
        self.user.set_password(u'password')
        self.user.save()
        self.photo = PhotoFactory.create(owner=self.user.profile,
                                         file=factory.django.ImageField())
        self.photo.save()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = u'Judy Hopps'
    email = u'Judy@zpd.gov'


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    title = u'Test'
    description = u'Here is my test photo'
    date_published = datetime.date.today()
