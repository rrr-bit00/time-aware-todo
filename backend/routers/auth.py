from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session

from schemas.auth import UserLogin
from models.user import User
from db.dependencies import get_db
from utils.security import hash_password, verify_password

router = APIRouter(prefix = "/auth",
            tags = ["auth"])

# ログイン用のエンドポイント
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    # 入力されたemailがdbに存在するか確認
    db_user = db.query(User).filter(User.email == user.email).first()
    # ユーザーが存在するか、パスワードが一致するか確認
    if not db_user or not verify_password(user.password,
        db_user.password):
        raise HTTPException(status_code = '401',
            detail = "Emailかパスワードが違います")