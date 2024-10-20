from django.test import TestCase
from django.urls import reverse
from api.tests.factories.worshiper_factory import WorshiperFactory


class WorshiperListViewTest(TestCase):
    def setUp(self):
        self.worshipers = WorshiperFactory.create_batch(3)

    def test_get(self):
        response = self.client.get(reverse("worshiper_list"))
        assert len(response.data) == 3
        assert response.status_code == 200
