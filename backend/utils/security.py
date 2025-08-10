from passlib.context import CryptContext

pass_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

# 生パスワードをハッシュ化
def hash_password(password: str) -> str:
    return pass_context.hash(password)

# 入力されたパスワードとハッシュ化したパスワードを比較
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pass_context.verify(plain_password, hashed_password)
