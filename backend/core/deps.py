from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from core.config import SECRET_KEY, ALGORITHM
from db.db_deps import get_db
from models.users import User

# 認証用のスキームを設定
oauth2_schemas = OAuth2PasswordBearer(tokenUrl = "auth/login")

# JWT認証が失敗したとき用の例外処理を記述
credentials_exception = HTTPException(
    status_code = .HTTP_401_UNAUTHORIZED,
    detail = "認証情報が無効です"
    headers = {"WWW-Authenticate": "Bearer"}
)

def get_current_user(token: str = Depends(oauth2_schemas), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception
    return user