from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_host: str = "0.0.0.0"
    app_port: int = 8000

    db_connection: str

    fs_root: str = "static"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()