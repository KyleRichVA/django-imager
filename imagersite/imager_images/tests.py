from django.test import TestCase, override_settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .models import Photo, Album
from imagersite.settings import BASE_DIR
import factory
import datetime
import os

# Create your tests here.


class PhotoTestCase(TestCase):

    def setUp(self):
        """Create a testing user"""
        self.user = UserFactory.create(username=u'Judy Hopps',
                                       email=u'Judy@zpd.gov')
        self.user.set_password(u'password')

    @override_settings(MEDIA_ROOT=os.path.join(BASE_DIR, 'tmp'))
    def test_photo_creation(self):
        """Test that a photo gets connected to a user profile"""
        self.assertTrue(len(self.user.profile.photos.all()) == 0)
        self.photo = PhotoFactory.create(owner=self.user.profile,
                                         file=factory.django.ImageField())
        self.photo.save()
        self.assertTrue(len(self.user.profile.photos.all()) == 1)

    def test_album_creation(self):
        """Test that a album gets connected to a user profile"""
        self.assertTrue(len(self.user.profile.albums.all()) == 0)
        self.album = AlbumFactory(owner=self.user.profile)
        self.album.save()
        self.assertTrue(len(self.user.profile.albums.all()) == 1)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

    date_published = datetime.date.today()


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    date_published = datetime.date.today()
