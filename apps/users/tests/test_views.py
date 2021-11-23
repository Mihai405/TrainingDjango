import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from apps.users.models import User
from apps.users.serializer import RegisterSerializer


# initialize the APIClient app
client = Client()

class SessionAuthTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="mihai@yahoo.com",
                                        first_name="mihai",
                                        last_name="mihai", )
        self.user.set_password("mihai")
        self.user.save()

        self.user2 = User.objects.create(email="mihai2@yahoo.com",
                                         first_name="mihai2",
                                         last_name="mihai2", )
        self.user2.set_password("mihai2")
        self.user2.save()

        self.valid_payload = {
            "email": "mihai@yahoo.com",
            "password": "mihai"
        }

    def test_create_auth_token(self):
        response = client.post(reverse('auth'), data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_auth_token(self):
        response = client.post(reverse('auth'), data=json.dumps(self.valid_payload), content_type='application/json')
        response = client.delete(reverse('auth'))
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        response = client.delete(reverse('auth'))
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

class ListUsersTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="mihai@yahoo.com",
                                        first_name="mihai",
                                        last_name="mihai", )
        self.user.set_password("mihai")
        self.user.save()

        self.user2 = User.objects.create(email="mihai2@yahoo.com",
                                         first_name="mihai2",
                                         last_name="mihai2",)
        self.user2.set_password("mihai2")
        self.user2.save()

    def test_list_users(self):
        response = client.get(reverse('user-list'))
        users = User.objects.all()
        serializer = RegisterSerializer(users,many=True)
        self.assertEqual(response.data,serializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

class CreateUserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="mihai@yahoo.com",
                                        first_name="mihai",
                                        last_name="mihai", )
        self.user.set_password("mihai")
        self.user.save()

        self.valid_payload = {
            "email": "new_user@yahoo.com",
            "first_name": "New",
            "last_name": "user",
            "password": "user"
        }

        self.invalid_payload = {
            "email": "mihai@yahoo.com",  # same email as user 1
            "first_name": "New",
            "last_name": "user",
            "password": "user"
        }

    def test_create_valid_user(self):
        response = client.post(reverse('user-list'),data=json.dumps(self.valid_payload),content_type='application/json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        response = client.post(reverse('user-list'), data=json.dumps(self.invalid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateUserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="mihai@yahoo.com",
                                        first_name="mihai",
                                        last_name="mihai", )
        self.user.set_password("mihai")
        self.user.save()

        self.valid_payload = {
            "email": "new_user@yahoo.com",
            "first_name": "New",
            "last_name": "user",
            "password": "user"
        }

    def test_update_valid_friend(self):
        response = client.put(
            reverse('user-detail', kwargs={'pk': self.user.id}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class DeleteUserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="mihai@yahoo.com",
                                        first_name="mihai",
                                        last_name="mihai", )
        self.user.set_password("mihai")
        self.user.save()

    def test_delete_valid_user(self):
        response = client.delete(
            reverse('user-detail', kwargs={'pk': self.user.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_user(self):
        response = client.delete('user-detail', kwargs={'pk': 2})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)