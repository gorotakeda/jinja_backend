FROM python:3.10-slim

# 作業ディレクトリの設定
WORKDIR /app

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    python3-dev \
    gcc \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# 依存関係のインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn==21.2.0

# ソースコードのコピー
COPY . .

# ログディレクトリの作成
RUN mkdir -p /var/log/django && \
    chmod 755 /var/log/django

# 環境変数の設定
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=jinja_backend.settings

# ポートの公開
EXPOSE 8000

# 起動コマンド
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "jinja_backend.wsgi:application"]
