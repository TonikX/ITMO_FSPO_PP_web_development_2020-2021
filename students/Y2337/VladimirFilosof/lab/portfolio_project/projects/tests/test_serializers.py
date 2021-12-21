from unittest import TestCase

from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.project_1 = Project.objects.create(
            title="Сайт визитка + интернет магазин", description="some text", preview="some reference"
        )

        self.project_2 = Project.objects.create(
            title="Текущий сайт", description="some other text",
            preview="some reference", project_url="url to project", code_url="source code if i want"
        )

    def test_get(self):
        data = ProjectSerializer([self.project_1, self.project_2], many=True).data
        expected_data = [
            {
                'id': self.project_1.id,
                'title': 'Сайт визитка + интернет магазин',
                'description': 'some text',
                'preview': 'some reference',
                'project_url': None,
                'code_url': None,
            },
            {
                'id': self.project_2.id,
                'title': 'Текущий сайт',
                'description': 'some other text',
                'preview': 'some reference',
                'project_url': 'url to project',
                'code_url': 'source code if i want',
            },
        ]

        self.assertEqual(expected_data, data)