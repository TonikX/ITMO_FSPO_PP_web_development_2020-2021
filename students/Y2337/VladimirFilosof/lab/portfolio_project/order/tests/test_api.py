import json

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from order.models import Service, User, Order
from order.serializers import ServiceSerializer, OrderSerializer


class ServiceAPITestCase(APITestCase):
    def setUp(self):
        self.admin = User.objects.create(username='admin', is_staff=True)
        self.admin.set_password('staffpassword')
        self.admin.save()

        self.token = Token.objects.create(user=self.admin)

        self.service1 = Service.objects.create(
            title="Test title 1", description="some short description",
            text="some long text", preview="url to preview"
        )
        self.service2 = Service.objects.create(
            title="Test title 2", description="some other short description",
            text="some other long text", preview="url to second preview"
        )

    def test_get(self):
        url = reverse('service-list')
        response = self.client.get(url)
        serializer_data = ServiceSerializer([self.service1, self.service2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, serializer_data)

    def test_create(self):
        url = reverse('service-list')

        user_data = {"username": "testuser", "password": "testpasstortestuser"}
        user_json = json.dumps(user_data)

        client = APIClient()

        client.post('/auth/users/', data=user_json, content_type='application/json')
        user = User.objects.get_by_natural_key('testuser')
        user.is_staff = True
        user.save()
        user_token = client.post('/auth/token/login/', data=user_json, content_type='application/json')

        data = {
            'title': 'Test title 1',
            'description': 'some short description',
            'text': 'some long text',
            'preview': 'url to preview',

        }
        json_data = json.dumps(data)

        client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.data['auth_token'])
        response = client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(3, Service.objects.all().count())
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_update(self):
        url = reverse('service-detail', args=(self.service1.id,))

        user_data = {"username": "testuser", "password": "testpasstortestuser"}
        user_json = json.dumps(user_data)

        client = APIClient()

        client.post('/auth/users/', data=user_json, content_type='application/json')
        user = User.objects.get_by_natural_key('testuser')
        user.is_staff = True
        user.save()
        user_token = client.post('/auth/token/login/', data=user_json, content_type='application/json')

        data = {
            'title': self.service1.title,
            'description': 'some short new description',
            'text': self.service1.text,
            'preview': self.service1.preview

        }
        json_data = json.dumps(data)

        client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.data['auth_token'])
        response = client.put(url, data=json_data, content_type='application/json')

        self.service1.refresh_from_db()
        serialized_data = ServiceSerializer(self.service1).data

        self.assertEqual(2, Service.objects.all().count())
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data['description'], data['description'])

    def test_delete(self):
        url = reverse('service-detail', args=(self.service1.id,))

        user_data = {"username": "testuser", "password": "testpasstortestuser"}
        user_json = json.dumps(user_data)

        client = APIClient()

        client.post('/auth/users/', data=user_json, content_type='application/json')
        user = User.objects.get_by_natural_key('testuser')
        user.is_staff = True
        user.save()
        user_token = client.post('/auth/token/login/', data=user_json, content_type='application/json')

        data = {
            'id': self.service1.id
        }
        json_data = json.dumps(data)

        client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.data['auth_token'])
        response = client.delete(url, data=json_data, content_type='application/json')

        self.assertEqual(1, Service.objects.all().count())
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_create_but_not_staff(self):
        url = reverse('service-list')

        user_data = {"username": "testuser", "password": "testpasstortestuser"}
        user_json = json.dumps(user_data)

        client = APIClient()

        client.post('/auth/users/', data=user_json, content_type='application/json')
        user = User.objects.get_by_natural_key('testuser')
        user.save()
        user_token = client.post('/auth/token/login/', data=user_json, content_type='application/json')

        data = {
            'title': 'Test title 1',
            'description': 'some short description',
            'text': 'some long text',
            'preview': 'url to preview',

        }
        json_data = json.dumps(data)

        client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.data['auth_token'])
        response = client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(2, Service.objects.all().count())
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_update_but_not_staff(self):
        url = reverse('service-detail', args=(self.service1.id,))

        user_data = {"username": "testuser", "password": "testpasstortestuser"}
        user_json = json.dumps(user_data)

        client = APIClient()

        client.post('/auth/users/', data=user_json, content_type='application/json')
        user = User.objects.get_by_natural_key('testuser')
        user.save()
        user_token = client.post('/auth/token/login/', data=user_json, content_type='application/json')

        data = {
            'id': self.service1.id,
            'title': self.service1.title,
            'description': 'some short new description',
            'text': self.service1.text,
            'preview': self.service1.preview

        }
        json_data = json.dumps(data)

        client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.data['auth_token'])
        response = client.put(url, data=json_data, content_type='application/json')

        service1_copy = self.service1
        self.service1.refresh_from_db()
        serialized_data = ServiceSerializer([self.service1, service1_copy], many=True).data

        self.assertEqual(2, Service.objects.all().count())
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.assertEqual(serialized_data[1], serialized_data[0])

    def test_delete_but_not_staff(self):
        url = reverse('service-detail', args=(self.service1.id,))

        user_data = {"username": "testuser", "password": "testpasstortestuser"}
        user_json = json.dumps(user_data)

        client = APIClient()

        client.post('/auth/users/', data=user_json, content_type='application/json')
        user = User.objects.get_by_natural_key('testuser')
        user.save()
        user_token = client.post('/auth/token/login/', data=user_json, content_type='application/json')

        data = {
        }
        json_data = json.dumps(data)

        client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.data['auth_token'])
        response = client.delete(url, data=json_data, content_type='application/json')

        self.assertEqual(2, Service.objects.all().count())
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_create_but_not_authentication(self):
        url = reverse('service-list')

        client = APIClient()

        data = {
            'title': 'Test title 1',
            'description': 'some short description',
            'text': 'some long text',
            'preview': 'url to preview',

        }
        json_data = json.dumps(data)

        response = client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(2, Service.objects.all().count())
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_update_but_not_authentication(self):
        url = reverse('service-detail', args=(self.service1.id,))

        client = APIClient()

        data = {
            'id': self.service1.id,
            'title': self.service1.title,
            'description': 'some short new description',
            'text': self.service1.text,
            'preview': self.service1.preview

        }
        json_data = json.dumps(data)

        response = client.put(url, data=json_data, content_type='application/json')

        service1_copy = self.service1
        self.service1.refresh_from_db()
        serialized_data = ServiceSerializer([self.service1, service1_copy], many=True).data

        self.assertEqual(2, Service.objects.all().count())
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
        self.assertEqual(serialized_data[1], serialized_data[0])

    def test_delete_but_not_authentication(self):
        url = reverse('service-detail', args=(self.service1.id,))

        client = APIClient()

        data = {
            'id': self.service1.id
        }
        json_data = json.dumps(data)

        response = client.delete(url, data=json_data, content_type='application/json')

        self.assertEqual(2, Service.objects.all().count())
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)


class OrderAPITestCase(APITestCase):
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

        self.order1 = Order.objects.create(
            user=self.user1, service=self.service1
        )
        self.order2 = Order.objects.create(
            user=self.user2, service=self.service2
        )

    def test_get(self):
        url = reverse('order-detail', args=(self.order1.id,))

        user_data = {"username": self.user1.username, "password": "testpass"}
        user_json = json.dumps(user_data)

        client = APIClient()

        user_token = client.post('/auth/token/login/', data=user_json, content_type='application/json')

        client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.data['auth_token'])
        response = client.get(url)
        serializer_data = OrderSerializer(self.order1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, serializer_data)

    def test_create(self):
        url = reverse('order-list')

        user_data = {"username": self.user1.username, "password": "testpass"}
        user_json = json.dumps(user_data)

        client = APIClient()

        user_token = client.post('/auth/token/login/', data=user_json, content_type='application/json')
        client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.data['auth_token'])

        data = {
            'user': self.user1.id,
            'service': self.service2.id
        }
        json_data = json.dumps(data)

        response = client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(3, Order.objects.all().count())
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_update(self):
        url = reverse('order-detail', args=(self.order1.id,))

        user_data = {"username": self.user1.username, "password": "testpass"}
        user_json = json.dumps(user_data)

        client = APIClient()

        user_token = client.post('/auth/token/login/', data=user_json, content_type='application/json')
        client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.data['auth_token'])

        data = {
            'user': self.user1.id,
            'service': self.service1.id
        }
        json_data = json.dumps(data)

        response = client.put(url, data=json_data, content_type='application/json')

        self.order1.refresh_from_db()
        serialized_data = OrderSerializer(self.order1).data

        self.assertEqual(2, Order.objects.all().count())
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data['service'], data['service'])

    def test_delete(self):
        url = reverse('order-detail', args=(self.order1.id,))

        user_data = {"username": self.user1.username, "password": "testpass"}
        user_json = json.dumps(user_data)

        client = APIClient()

        user_token = client.post('/auth/token/login/', data=user_json, content_type='application/json')

        client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.data['auth_token'])
        response = client.delete(url, content_type='application/json')

        self.assertEqual(1, Order.objects.all().count())
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_get_but_not_authentication(self):
        url = reverse('order-list')

        client = APIClient()

        response = client.get(url)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_create_but_not_authentication(self):
        url = reverse('order-list')

        client = APIClient()

        data = {
            'user': self.user1.id,
            'service': self.service2.id
        }
        json_data = json.dumps(data)

        response = client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(2, Service.objects.all().count())
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_update_but_not_authentication(self):
        url = reverse('order-detail', args=(self.order1.id,))

        client = APIClient()

        data = {
            'user': self.user1.id,
            'service': self.service2.id
        }
        json_data = json.dumps(data)

        response = client.put(url, data=json_data, content_type='application/json')

        self.order1.refresh_from_db()
        serialized_data = OrderSerializer(self.order1).data

        self.assertEqual(2, Order.objects.all().count())
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
        self.assertEqual(serialized_data['service'], self.service1.id)

    def test_delete_but_not_authentication(self):
        url = reverse('order-detail', args=(self.order1.id,))

        client = APIClient()

        response = client.delete(url, content_type='application/json')

        self.assertEqual(2, Order.objects.all().count())
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)