import secrets
import warnings

from typing import Annotated, Any, Literal
from typing_extensions import Self
from pydantic import (
    AnyUrl,
    BeforeValidator,
    EmailStr,
    HttpUrl,
    PostgresDsn,
    computed_field,
    model_validator,
)
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


# CORS設定
def parse_cors(origin: Any) -> list[str] | str:
    # 文字列かチェック
    if isinstance(origin, str) and not origin.startswith("["):
        return [i.strip() for i in origin.split(",")]
    elif isinstance(origin, list | str):
        return origin
    raise ValueError(origin)


# 環境変数をPythonオブジェクトに変換して読み込む
class Settings(BaseSettings):
    # 環境変数を設定
    model_config = SettingsConfigDict(
        env_file="../.env", env_ignore_empty=True, extra="ignore"
    )
    # APIのバージョン1のパス
    API_V1_STR: str = "/api/v1"
    # jwtなどに使用するランダムな文字列の生成
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # トークンの有効時間を分単位で設定
    ACCESS_TOKEN_EXPINE_MINUTES: int = 60 * 24 * 8
    # CORS用のフロントエンドのURLを設定
    FRONTEND_HOST: str = "http://localhost:5173"
    # 開発、テスト、本番用に環境を分ける値を作成
    ENVIRONMENT: Literal["local", "starting", "production"] = "local"

    # CORSがlist[AnyUrl]かstrかチェック
    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []

    # バックエンドとフロントエンドのURLをつなげる
    @computed_field
    @property
    def all_cors_origins(self) -> list[str]:
        # 末尾が/ならば削除してつなげる
        return [str(origin).rstrip("/") for origin in self.BACKEND_CORS_ORIGINS] + [
            self.FRONTEND_HOST
        ]

    # PostgreSQLの環境変数を受けとる際のスキーマ
    PROJECT_NAME: str
    SENTRY_DSN: HttpUrl | None = None
    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = ""

    # PostgreSQLのURLを作成
    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URL(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )

    # 管理者のEmailとpass
    FIRST_SUPERUSER: EmailStr
    FIRST_SUPERUSER_PASSWORD: str

    # passなどが暗号化されているか確認
    def _check_default_secret(self, var_name: str, value: str | None) -> None:
        # changethisはサンプル
        if value == "changethis":
            message = (
                f'The value of {var_name} is "changethis", '
                "for security, please change it, at least for deployments."
            )
            # 開発環境なら、warningで警告
            if self.ENVIRONMENT == "local":
                warnings.warn(message, stacklevel=1)
            # 開発環境以外なら、ValueErrorでエラー
            else:
                raise ValueError(message)

    # mode=afterで最後に実行
    @model_validator(mode="after")
    def _enforce_non_default_secrets(self) -> Self:
        self._check_default_secret("SECRET_KEY", self.SECRET_KEY)
        self._check_default_secret("POSTGRES_PASSWORD", self.POSTGRES_PASSWORD)
        self._check_default_secret(
            "FIRST_SUPERUSER_PASSWORD", self.FIRST_SUPERUSER_PASSWORD
        )

        return self


setting = Settings()
