# dbとの接続情報や設定を保持するためのファイル
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import setting

# dbエンジンの生成
engine = create_engine(setting.SQLALCHEMY_DATABASE_URL, echo=True)

# セッションクラスの作成（autocommitやautoflushの設定）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
