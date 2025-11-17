from datetime import datetime, timedelta, timezone
from typing import Any
from jose import jwt
from passlib.context import CryptContext

from config import setting

pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


# 生パスワードをハッシュ化
def hash_password(password: str) -> str:
    return pass_context.hash(password)


# 入力されたパスワードとDBに保存したハッシュ化したパスワードを比較
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pass_context.verify(plain_password, hashed_password)


# 特定の期間使用できるJWTトークンを発行する関数
def create_access_token(
    subject: str | Any,  # トークンに含めたいデータ（例: ユーザーIDなど）
    expires_minutes: timedelta,
) -> str:
    # 現在時刻（UTC）から分単位で有効期限を計算
    exp = datetime.now(timezone.utc) + expires_minutes
    to_encode = {"exp": exp, "sub": subject}
    encoded_jwt = jwt.encode(to_encode, setting.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
