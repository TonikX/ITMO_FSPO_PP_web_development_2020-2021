from django.urls import reverse
from rest_framework import status
from rest_framework.utils import json

from feedback.models import Feedback
from feedback.serializers import FeedbackSerializer
from order.models import User, Service
from rest_framework.test import APITestCase, APIClient


class FeedbackAPITestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='user1')
        self.user1.set_password('testpass')
        self.user1.save()
        self.user2 = User.objects.create(username='user2')
        self.user2.set_password('testpass')
        self.user2.save()

        self.service1 = Service.objects.create(
            title="Test title 1", description="some short description",
            text="some long text", preview="url to preview"
        )
        self.service2 = Service.objects.create(
            title="Test title 2", description="some other short description",
            text="some other long text", preview="url to second preview"
        )

        self.feedback1 = Feedback.objects.create(
            is_global=False, user=self.user1,
            service=self.service1, text="Feedback text", img="url to preview"
        )
        self.feedback2 = Feedback.objects.create(
            is_global=True, user=self.user2,
            service=None, text="Global feedback text", img=None
        )

    def test_get(self):
        url = reverse('feedback-list')
        response = self.client.get(url)
        serializer_data = FeedbackSerializer([self.feedback1, self.feedback2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, serializer_data)

    def test_create(self):
        url = reverse('feedback-list')

        user_data = {"username": "user1", "password": "testpass"}
        user_json = json.dumps(user_data)

        client = APIClient()

        user_token = client.post('/auth/token/login/', data=user_json, content_type='application/json')

        data = {
            'is_global': False,
            'service': self.service2.id,
            'text': "Feedback text",
            'img': "url to preview"
        }
        json_data = json.dumps(data)

        client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.data['auth_token'])
        response = client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, Feedback.objects.all().count())

    def test_update(self):
        url = reverse('feedback-detail', args=(self.feedback1.id,))

        user_data = {"username": "user1", "password": "testpass"}
        user_json = json.dumps(user_data)

        client = APIClient()

        user_token = client.post('/auth/token/login/', data=user_json, content_type='application/json')

        data = {
            'is_global': False,
            'user': self.user1.id,
            'service': self.service1.id,
            'text': "Feedback text",
            'img': "url to preview"
        }
        json_data = json.dumps(data)

        client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.data['auth_token'])
        response = client.put(url, data=json_data, content_type='application/json')

        self.service1.refresh_from_db()
        serialized_data = FeedbackSerializer(self.feedback1).data

        self.assertEqual(2, Feedback.objects.all().count())
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data['service'], self.service1.id)

    def test_delete(self):
        url = reverse('feedback-detail', args=(self.feedback1.id,))

        user_data = {"username": "user1", "password": "testpass"}
        user_json = json.dumps(user_data)

        client = APIClient()

        user_token = client.post('/auth/token/login/', data=user_json, content_type='application/json')

        client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.data['auth_token'])
        response = client.delete(url, content_type='application/json')

        self.assertEqual(1, Feedback.objects.all().count())
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_create_but_not_authentication(self):
        url = reverse('feedback-list')

        client = APIClient()

        data = {
            'is_global': False,
            'user': self.user1.id,
            'service': self.service2.id,
            'text': "Feedback text",
            'img': "url to preview"
        }
        json_data = json.dumps(data)

        response = client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
        self.assertEqual(2, Feedback.objects.all().count())

    def test_update_but_not_authentication(self):
        url = reverse('feedback-detail', args=(self.feedback1.id,))

        client = APIClient()

        data = {
            'is_global': False,
            'user': self.user1.id,
            'service': self.service1.id,
            'text': "Feedback text",
            'img': "url to preview"
        }
        json_data = json.dumps(data)

        response = client.put(url, data=json_data, content_type='application/json')

        self.service1.refresh_from_db()
        serialized_data = FeedbackSerializer(self.feedback1).data

        self.assertEqual(2, Feedback.objects.all().count())
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_delete_but_not_authentication(self):
        url = reverse('feedback-detail', args=(self.feedback1.id,))

        client = APIClient()

        response = client.delete(url, content_type='application/json')

        self.assertEqual(2, Feedback.objects.all().count())
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
