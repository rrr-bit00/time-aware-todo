# dbとの接続情報や設定を保持するためのファイル
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
load_dotenv()

# 使用できるようにos.getenvで呼び出す
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
# .envにHOSTとPORTを記述していないため、デフォルト値を設定
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

# dbの接続URL
SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

# dbエンジンの生成
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo = True)

# セッションクラスの作成（autocommitやautoflushの設定）
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
