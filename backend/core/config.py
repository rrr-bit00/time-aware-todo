# 開発用
import os

MODE = os.getenv("MODE", "DEV").upper()
SECRET_KEY = os.getenv("SECRET_KEY", "QjaRK3cBkIl9/qlgcR/Di3irNmTACECEyOVD8mL5bDu+EqC2LzBLC6ZIOZCGowGsbfMOc0WOYrWR6yxnbvH6UA==")

# 共有カギを使用するため、HS256をデフォルト値に設定
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))


""" デモの際に以下のマルチコメントの中身を使用する
import os
from dotenv import load_dotenv

load_dotenv()

MODE = os.getenv("MODE").upper()
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is required in non-DEV mode.")

# 共有カギを使用するため、HS256をデフォルト値に設定
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
"""