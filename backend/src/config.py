from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    CMC_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Setting()



