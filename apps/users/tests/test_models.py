from django.test import TestCase
from apps.users.models import User

class UserTest(TestCase):

    def setUp(self):
        self.user=User.objects.create(email="mihai@yahoo.com",
                                first_name="mihai",
                                last_name= "mihai",)
        self.user.set_password("mihai")
        self.user.save()

        self.user2 = User.objects.create(email="mihai2@yahoo.com",
                                        first_name="mihai2",
                                        last_name="mihai2",)
        self.user2.set_password("mihai2")
        self.user2.save()

    def test_email(self): #verify if the email is saved correctly
        self.assertEqual(self.user.email, 'mihai@yahoo.com')
        self.assertNotEqual(self.user.email, 'mihai2@yahoo.com')
        self.assertEqual(self.user2.email, 'mihai2@yahoo.com')

    def test_first_name(self): #verify if the first_name is saved correctly
        self.assertEqual(self.user.first_name,'mihai')
        self.assertNotEqual(self.user.first_name,'mihai2')
        self.assertEqual(self.user2.first_name,'mihai2')

    def test_last_name(self): #verify if the last_name is saved correctly
        self.assertEqual(self.user.last_name,'mihai')
        self.assertNotEqual(self.user.last_name,'mihai2')
        self.assertEqual(self.user2.last_name,'mihai2')

    def test_password(self): #verify if the password is saved correctly
        assert self.user.check_password('mihai')
        assert self.user2.check_password('mihai2')