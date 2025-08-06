from pydantic import BaseModel, EmailStr

# Usersテーブルの共通フィールドを定義
class UserBase(BaseModel):
    username: str
    email: EmailStr

# アカウント作成時のフィールドを定義
class UserCreate(UserBase):
    hash_pass: str

# 読み込む際の、フィールドを定義
class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True
