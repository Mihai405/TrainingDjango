import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from apps.friends.models import Friend
from apps.friends.serializers import FriendSerializer
from apps.users.models import User
import jwt

# initialize the APIClient app
client = Client()

class GetAllFriendsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="mihai@yahoo.com",
                                   first_name="mihai",
                                   last_name="mihai")
        self.user.set_password("mihai")
        self.user.save()

        user2 = User.objects.create(email="mihai2@yahoo.com",
                                   first_name="mihai2",
                                   last_name="mihai2")
        user2.set_password("mihai")
        user2.save()

        """
        payload = {
            'id': user.id,
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        session = self.client.session
        session["user"]= token
        session.save()
        
        self.valid_payload = {
            "email": "mihai@yahoo.com",
            "password": "mihai"
        }
        response = client.post(reverse('login'), data=json.dumps(self.valid_payload), content_type='application/json')
        
        """

        self.valid_payload = {
            "email": "mihai@yahoo.com",
            "password": "mihai"
        }
        response = client.post(reverse('login'), data=json.dumps(self.valid_payload), content_type='application/json')

        Friend.objects.create(
            first_name='User1', last_name='User1', phone_number='073457891', user=self.user)
        Friend.objects.create(
            first_name='User2', last_name='User2', phone_number='073457892', user=self.user)
        Friend.objects.create(
            first_name='User3', last_name='User3', phone_number='073457893', user=self.user)
        Friend.objects.create(
            first_name='User4', last_name='User4', phone_number='073457894', user=self.user)
        Friend.objects.create(
            first_name='User5', last_name='User5', phone_number='073457895', user=self.user)

    def test_get_all_friends(self):
        # get API response
        response = client.get(reverse('friends'))
        # get data from db
        friends = Friend.objects.filter(user=User.objects.get(id=1))
        serializer = FriendSerializer(friends, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateNewFriendTest(TestCase):
    def setUp(self):
        user = User.objects.create(email="mihai@yahoo.com",
                                   first_name="mihai",
                                   last_name="mihai")
        user.set_password("mihai")
        user.save()
        self.valid_payload = {
            "email": "mihai@yahoo.com",
            "password": "mihai"
        }
        response = client.post(reverse('login'), data=json.dumps(self.valid_payload), content_type='application/json')

        self.valid_friend_payload = {
            "first_name": "New User",
            "last_name": "New User",
            "phone_number": "0734578900"
        }

        self.invalid_friend_payload = {
            "first_name": "New User",
            "last_name": "New User",
            "phone_number": "073457890"
        }

    def test_create_valid_friend(self):
        response = client.post(reverse('friends'), data=json.dumps(self.valid_friend_payload), content_type='application/json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_create_invalid_friend_phone_number(self):
        response = client.post(reverse('friends'), data=json.dumps(self.invalid_friend_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.invalid_friend_payload['phone_number']="1073457890"
        response = client.post(reverse('friends'), data=json.dumps(self.invalid_friend_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.invalid_friend_payload['phone_number'] = "a07347890"
        response = client.post(reverse('friends'), data=json.dumps(self.invalid_friend_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateFriendTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="mihai@yahoo.com",
                                   first_name="mihai",
                                   last_name="mihai")
        self.user.set_password("mihai")
        self.user.save()
        self.valid_payload = {
            "email": "mihai@yahoo.com",
            "password": "mihai"
        }
        response = client.post(reverse('login'), data=json.dumps(self.valid_payload),content_type='application/json')

        self.friend=Friend.objects.create(
            first_name='User1', last_name='User1', phone_number='073457891', user=self.user)

        self.valid_friend_payload = {
            "first_name": "New User",
            "last_name": "New User",
            "phone_number": "0734578900"
        }

        self.invalid_friend_payload = {
            "first_name": "New User",
            "last_name": "New User",
            "phone_number": "073457890098089099089089"
        }


    def test_update_valid_friend(self):
        response = client.put(
            reverse('update_friend', kwargs={'pk': self.friend.id}),
            data=json.dumps(self.valid_friend_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_friend(self):
        response = client.put(
            reverse('update_friend', kwargs={'pk': self.friend.id}),
            data=json.dumps(self.invalid_friend_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteFriendTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="mihai@yahoo.com",
                                   first_name="mihai",
                                   last_name="mihai")
        self.user.set_password("mihai")
        self.user.save()
        self.valid_payload = {
            "email": "mihai@yahoo.com",
            "password": "mihai"
        }
        response = client.post(reverse('login'), data=json.dumps(self.valid_payload),content_type='application/json')

        self.friend=Friend.objects.create(
            first_name='User1', last_name='User1', phone_number='073457891', user=self.user)
        self.friend = Friend.objects.create(
            first_name='User2', last_name='User2', phone_number='073457892', user=self.user)
        self.friend = Friend.objects.create(
            first_name='User3', last_name='User3', phone_number='073457893', user=self.user)

    def test_delete_valid_friend(self):
        response = client.delete(
            reverse('update_friend', kwargs={'pk': self.friend.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_friend(self):
        response = client.delete(
            reverse('update_friend', kwargs={'pk':100}))
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)