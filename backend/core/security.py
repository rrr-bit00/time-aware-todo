from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional
from jose import jwt
from passlib.context import CryptContext

from core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pass_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

# 生パスワードをハッシュ化
def hash_password(password: str) -> str:
    return pass_context.hash(password)

# 入力されたパスワードとDBに保存したハッシュ化したパスワードを比較
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pass_context.verify(plain_password, hashed_password)

# 特定の期間使用できるJWTトークンを発行する関数
def create_access_token(
    data: Dict[str, Any],                       # トークンに含めたいデータ（例: ユーザーIDなど）
    expires_minutes: Optional[int] = None       # 有効期限（分単位）。指定なしならデフォルト値を使う
) -> str:
    # 元データをコピー（元の引数dataを直接変更しないため）
    payload = data.copy()

    # 現在時刻（UTC）から有効期限を計算
    # expires_minutes が指定されていればそれを使い、
    # 指定がなければ ACCESS_TOKEN_EXPIRE_MINUTES（デフォルト値）を使う
    exp = datetime.now(timezone.utc) + timedelta(
        minutes = expires_minutes or ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # JWTの標準クレーム "exp" に有効期限を追加
    payload.update({"exp": exp})

    # JWTを署名付きでエンコードして文字列として返す
    # SECRET_KEY と ALGORITHM で改ざん防止のための署名を行う
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
