# Generated by Django 3.2.5 on 2024-10-20 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Worshiper",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("last_name", models.CharField(max_length=50, verbose_name="姓")),
                ("first_name", models.CharField(max_length=50, verbose_name="名")),
                (
                    "last_name_kana",
                    models.CharField(max_length=50, verbose_name="姓（かな）"),
                ),
                (
                    "first_name_kana",
                    models.CharField(max_length=50, verbose_name="名（かな）"),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "男性"), ("female", "女性")],
                        max_length=10,
                        verbose_name="性別",
                    ),
                ),
                (
                    "birthday",
                    models.DateField(blank=True, null=True, verbose_name="生年月日"),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, max_length=15, null=True, verbose_name="電話番号"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="メールアドレス",
                    ),
                ),
                (
                    "visited_day",
                    models.DateField(blank=True, null=True, verbose_name="参拝日"),
                ),
                (
                    "post_code",
                    models.CharField(
                        blank=True, max_length=8, null=True, verbose_name="郵便番号"
                    ),
                ),
                (
                    "prefecture",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="都道府県"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="市区町村"
                    ),
                ),
                (
                    "street_address",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="町名・番地"
                    ),
                ),
                (
                    "building_name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="建物名"
                    ),
                ),
                ("note", models.TextField(blank=True, null=True, verbose_name="備考")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="有効フラグ"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="作成日時"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="更新日時"),
                ),
            ],
            options={
                "verbose_name": "参拝者",
                "verbose_name_plural": "参拝者一覧",
            },
        ),
    ]
