from django.test import TestCase
from apps.friends.models import Friend
from apps.users.models import User

class FriendTest(TestCase):

    def setUp(self):
        self.user=User.objects.create(email="mihai@yahoo.com",
                                first_name="mihai",
                                last_name= "mihai",)
        self.user.set_password("mihai")
        self.user.save()
        Friend.objects.create(first_name='User1',last_name='User1',phone_number='073457891',user=self.user)
        Friend.objects.create(first_name='User2', last_name='User2', phone_number='073457892',user=self.user)

    def test_first_name(self):
        friend1=Friend.objects.get(id=1)
        friend2=Friend.objects.get(id=2)
        self.assertEqual(friend1.first_name,'User1')
        self.assertNotEqual(friend1.last_name,'User12')
        self.assertEqual(friend2.first_name,'User2')

    def test_last_name(self):
        friend1=Friend.objects.get(id=1)
        friend2=Friend.objects.get(id=2)
        self.assertEqual(friend1.last_name,'User1')
        self.assertNotEqual(friend1.last_name,'User12')
        self.assertEqual(friend2.last_name,'User2')

    def test_phone_number(self):
        friend1=Friend.objects.get(id=1)
        friend2=Friend.objects.get(id=2)
        self.assertEqual(friend1.phone_number,'073457891')
        self.assertEqual(friend2.phone_number,'073457892')