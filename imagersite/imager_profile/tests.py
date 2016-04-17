from django.test import TestCase
from imager_profile.models import User_Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
import factory

# Create your tests here.


class ProfileTestCase(TestCase):

    def setUp(self):
        """Create a user object to use throughout tests."""
        self.user = UserFactory.create(username=u'Judy',
                                       email=u'Hopps@zpd.gov')
        self.user.set_password(u'password')
        self.profile = self.user.profile

    def test_user_has_profile(self):
        """Test that a django user has a profile connected to it after save."""
        self.test = User(username=u'Nick', email=u'Wilde@zpd.gov')
        self.test.set_password(u'carrots')
        with self.assertRaises(ObjectDoesNotExist):
            self.test.profile
        self.test.save()
        self.assertTrue(self.test.profile)

    def test_profile_deletes_with_user(self):
        # We have one profile/user currently.
        self.assertTrue(self.profile in User_Profile.objects.all())
        self.user.delete()
        # Now there should be no profiles.
        self.assertFalse(self.profile in User_Profile.objects.all())

    def test_friend_connection(self):
        self.friend = UserFactory.create(username=u'Nick',
                                         email=u'Nick@zpd.gov')
        self.assertFalse(self.friend.profile in self.profile.friends.all())
        self.profile.friends.add(self.friend.profile)
        self.assertTrue(self.friend.profile in self.profile.friends.all())

    def test_is_active(self):
        """Test that the profile is_active matches with the User is_active."""
        self.assertEquals(self.profile.is_active, self.user.is_active)

    def test_active_manager(self):
        """Test the .active gives back all active profiles."""
        self.assertEquals(User_Profile.active.all()[0], self.profile)
        self.user.is_active = False
        self.user.save()
        self.assertFalse(self.profile in User_Profile.active.all())


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
