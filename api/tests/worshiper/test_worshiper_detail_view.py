from django.test import TestCase
from django.urls import reverse
from api.tests.factories.worshiper_factory import WorshiperFactory


class WorshiperDetailViewTest(TestCase):
    def setUp(self):
        self.worshiper = WorshiperFactory.create()

    def test_get_worshiper_detail_success(self):
        response = self.client.get(
            reverse("worshiper_detail", kwargs={"pk": self.worshiper.id})
        )
        assert response.status_code == 200

    def test_get_worshiper_detail_not_found(self):
        response = self.client.get(reverse("worshiper_detail", kwargs={"pk": 9999}))
        assert response.status_code == 404
        assert response.data["detail"] == "対象の参拝者が存在しません"
