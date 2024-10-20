import os
import sys
import django
from django.test import TestCase
from django.urls import reverse
from api.tests.factories.worshiper_factory import WorshiperFactory

# プロジェクトのルートディレクトリをパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jinja_backend.settings")
django.setup()


class WorshiperListViewTest(TestCase):
    def setUp(self):
        self.worshipers = WorshiperFactory.create_batch(5)

    def test_get(self):
        response = self.client.get(reverse("worshiper_list"))
        assert len(response.data) == 5
        assert response.status_code == 200
