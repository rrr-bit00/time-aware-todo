from pydantic import EmailStr
from sqlmodel import Field, SQLModel


# Usersテーブルの共通フィールドを定義
class UserBase(SQLModel):
    username: str | None = Field(default=None, index=True, max_length=255)
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool = Field(default=True)
    is_superuser = False


# アカウント作成時のフィールドを定義
class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=20)


# アカウント作成時のフィールドを定義（ユーザー）
class UserRegister(SQLModel):
    username: str | None = Field(default=None, max_length=255)
    email: EmailStr = Field(max_length=255)
    password: str = Field(min_length=8, max_length=29)


# emailかpasswordの更新
class UserUpdate(UserBase):
    # 更新しない方を送る必要がないためNoneを許可
    email: EmailStr | None = Field(default=None, max_length=255)
    password: str | None = Field(default=None, min_length=8, max_length=20)


# emailかpassowrdの更新（ユーザー）
class UserUpdateMe(SQLModel):
    username: str | None = Field(default=None, max_length=255)
    email: EmailStr | None = Field(default=None, max_length=255)


# passwordの更新（ユーザー）
class PasswordUpdate(SQLModel):
    current_password: str = Field(min_length=8, max_length=20)
    new_password: str = Field(min_length=8, max_length=20)


# 読み込む際の、フィールドを定義
class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True
