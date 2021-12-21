from django.test import TestCase

from order.models import Service
from order.serializers import ServiceSerializer


class ServiceSerializerTestCase(TestCase):
    def test_ok(self):
        self.service1 = Service.objects.create(
            title="Test title 1", description="some short description",
            text="some long text", preview="url to preview"
        )
        self.service2 = Service.objects.create(
            title="Test title 2", description="some other short description",
            text="some other long text", preview="url to second preview"
        )

        serializer_data = ServiceSerializer([self.service1, self.service2], many=True).data

        expected_data = [
            {
                'id': self.service1.id,
                'title': 'Test title 1',
                'description': 'some short description',
                'text': 'some long text',
                'preview': 'url to preview',
            },
            {
                'id': self.service2.id,
                'title': 'Test title 2',
                'description': 'some other short description',
                'text': 'some other long text',
                'preview': 'url to second preview',
            },
        ]

        self.assertEqual(serializer_data, expected_data)