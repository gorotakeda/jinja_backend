from django.db import models


class Worshiper(models.Model):
    last_name = models.CharField(max_length=50, verbose_name="姓")
    first_name = models.CharField(max_length=50, verbose_name="名")
    last_name_kana = models.CharField(max_length=50, verbose_name="姓（かな）")
    first_name_kana = models.CharField(max_length=50, verbose_name="名（かな）")
    gender = models.CharField(
        max_length=10,
        choices=[("male", "男性"), ("female", "女性")],
        verbose_name="性別",
    )
    birthday = models.DateField(blank=True, null=True, verbose_name="生年月日")
    phone_number = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="電話番号"
    )
    email = models.EmailField(blank=True, null=True, verbose_name="メールアドレス")
    visited_day = models.DateField(blank=True, null=True, verbose_name="参拝日")
    post_code = models.CharField(
        max_length=8, blank=True, null=True, verbose_name="郵便番号"
    )
    prefecture = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="都道府県"
    )
    city = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="市区町村"
    )
    street_address = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="町名・番地"
    )
    building_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="建物名"
    )
    note = models.TextField(blank=True, null=True, verbose_name="備考")
    is_active = models.BooleanField(default=True, verbose_name="有効フラグ")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "参拝者"
        verbose_name_plural = "参拝者一覧"
