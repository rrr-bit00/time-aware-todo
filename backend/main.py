from fastapi import FastAPI
from models.users import Base
from db.session import engine
from router import users

app = FastAPI()

# dbのテーブルを作成
Base.metadata.create_all(bind=engine)

# usersルーターをappに登録
app.include_router(users.router)
