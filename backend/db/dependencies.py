# db接続や認証の関数を自動でFastAPIに渡すファイル
from sqlalchemy.orm import Session
from session import SessionLocal

def get_db() -> Session:
    # dbと接続させる
    db = SessionLocal()
    # エラーが起きてもdbを閉じるためtryを使用
    try:
        yield db
    finally:
        db.close()
