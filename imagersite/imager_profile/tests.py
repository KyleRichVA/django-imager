from django.test import TestCase
from models import User_Profile
from django.contrib.auth.models import User
import factory

# Create your tests here.


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.user.set_password(u'password')
        self.user.save()

    def test_foo(self):
        import pdb; pdb.set_trace()
        self.assertTrue(False)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = u'Judy Hopps'
    email = u'Judy@zpd.gov'
