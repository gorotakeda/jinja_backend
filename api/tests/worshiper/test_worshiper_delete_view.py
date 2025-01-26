from django.test import TestCase
from django.urls import reverse
from api.tests.factories.worshiper_factory import WorshiperFactory


class WorshiperDeleteViewTest(TestCase):
    def setUp(self):
        self.worshiper = WorshiperFactory.create()

    def test_delete_worshiper_success(self):
        response = self.client.delete(
            reverse("worshiper_delete", kwargs={"pk": self.worshiper.id})
        )
        assert response.status_code == 200
        assert response.data["detail"] == "参拝者を削除しました。"

    def test_delete_worshiper_not_found(self):
        response = self.client.delete(reverse("worshiper_delete", kwargs={"pk": 9999}))
        assert response.status_code == 404
        assert response.data["detail"] == "対象の参拝者が存在しません"
