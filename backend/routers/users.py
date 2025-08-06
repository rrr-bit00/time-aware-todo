from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserRead
from models.user import User
from typing import List

router = APIRouter()


@router.post("/users", response_model = UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    # Uniqueフィールド（email）の重複を確認
    existng = db.query(User).filter(User.email == user.email).first()
    if existng:
        raize HTTPException(status = 400, detail = "このEmailはすでに登録されています")

    # 入力された辞書型の値を展開してdb_userに代入
    db_user = models.User(**user.dict())    # ** で辞書を展開
    db.add(db_user)                         # 作成したレコードを追加
    db.commit()                             # dbに変更を保存
    db.refresh(db_user)                     # 保存後に、idなどが自動生成されるため再読み込み
    return db_user                          # 完了後、クライアントサイドに情報を返す

