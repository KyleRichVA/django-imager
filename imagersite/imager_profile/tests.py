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
        self.assertTrue(len(User_Profile.objects.all()) == 1)
        self.user.delete()
        # Now there should be no profiles.
        self.assertTrue(len(User_Profile.objects.all()) == 0)

    def test_friend_connection(self):
        import pdb; pdb.set_trace()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
