from django.test import TestCase
from models import User_Profile, User_Manager
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
import factory

# Create your tests here.


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.user.set_password(u'password')
        self.user.save()

    def test_user_has_profile(self):
        """Test that a django user has a profile connected to it."""
        self.assertIsInstance(self.user.profile, User_Profile)

    def test_profile_good(self):
        """Test the profile has all its properties."""
        long_str = u"A"*350
        profile = self.user.profile
        #friend = self.user.profile.friends.create()
        self.assertFieldOutput(profile.camera_model,
                               {u'A Camera': u'A Camera'},
                               {long_str: ['max_length']})
        self.assertFieldOutput(profile.photo_type,
                               {u'Photos': u'Photos'},
                               {long_str: MaxLengthValidator})
        self.assertFieldOutput(profile.region,
                               {u'USA': u'USA'},
                               {long_str: MaxLengthValidator})
        self.assertIsInstance(profile.user, User)
        #self.assertIn(profile.friends, friend)
        self.assertTrue(profile.is_active)
        self.assertIsInstance(profile.active, User_Manager)
        self.assertIn(User.profile.active.all(), profile)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = u'Judy Hopps'
    email = u'Judy@zpd.gov'
