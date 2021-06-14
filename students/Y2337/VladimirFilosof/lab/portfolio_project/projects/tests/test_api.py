from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectAPITestCase(APITestCase):
    def test_get(self):
        project_1 = Project.objects.create(
            title="Сайт визитка + интернет магазин", description="some text", preview="some reference"
        )

        project_2 = Project.objects.create(
            title="Текущий сайт", description="some other text",
            preview="some reference", project_url="url to project", code_url="source code if i want"
        )

        url = reverse('project-list')
        response = self.client.get(url)
        serializer_data = ProjectSerializer([project_1, project_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
