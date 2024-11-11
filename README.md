# jinja_backend

# アプリケーション起動
```bash
python manage.py runserver
```

# コードのチェック
```bash
black .
```

# コードのチェック(Lint)
```bash
flake8
```

# テストコード実行
```bash
python manage.py test api.tests.ファイル名
例:python manage.py test api.tests.worshiper.test_worshiper_list_view
```

# テストコードのデータベースの初期化
```bash
python manage.py migrate --fake api zero
```

# seedデータ挿入
```bash
python manage.py loaddata seed_data.json
```

# 新しいパッケージをインストールした後に実行
```bash
pip freeze > requirements.txt
```
