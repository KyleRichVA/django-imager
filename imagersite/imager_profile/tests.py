from django.test import TestCase
from imagersite.imager_profile.models import User_Profile
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
import factory

# Create your tests here.


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.user.set_password(u'password')
        self.user.save()
        self.user.profile.camera_model = u"A Camera"
        self.user.profile.photo_type = u"Great Photos"
        self.user.profile.region = u'USA'
        friend = User(username=u'Nick', email=u'Nick@zpd.gov')
        friend.set_password(u'secret')
        friend.save()
        self.user.profile.friends.add(friend.profile)

    def test_user_has_profile(self):
        """Test that a django user has a profile connected to it."""
        self.assertIsInstance(self.user.profile, User_Profile)

    def test_profile_good(self):
        """Test the profile has all its properties."""
        profile = self.user.profile
        self.assertEqual(profile.camera_model, u"A Camera")
        self.assertEqual(profile.photo_type, u"Great Photos")
        self.assertEqual(profile.region, u"USA")
        self.assertIsInstance(profile.user, User)
        self.assertTrue(profile.friends)
        self.assertTrue(profile.is_active)
        self.assertEqual(User_Profile.active.all()[0], profile)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = u'Judy Hopps'
    email = u'Judy@zpd.gov'
