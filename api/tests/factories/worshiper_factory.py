import factory

from api.models.worshiper import Worshiper


class WorshiperFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Worshiper

    last_name = "山田"
    first_name = "太郎"
    last_name_kana = "ヤマダ"
    first_name_kana = "タロウ"
    gender = "male"
    birthday = "1990-01-01"
    post_code = "123-4567"
    prefecture = "東京都"
    city = "千代田区"
    street_address_1 = "永田町1-2-3"
    email = "yamada@example.com"
    phone_number = "09012345678"
    is_active = True
