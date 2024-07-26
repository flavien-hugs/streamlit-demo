from functools import lru_cache
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings


class StreamlitAPPConfig(BaseSettings):
    APP_TITLE: str = Field(default="Streamlit APP", alias="APP_TITLE")
    DEFAULT_PAGE_COLUMN: int = Field(default=2, alias="DEFAULT_PAGE_COLUMN")
    IMAGE_TYPE: List[str] = Field(default=['png', 'jpg', 'jpeg'], alias="IMAGE_TYPE")


@lru_cache
def get_settings() -> StreamlitAPPConfig:
    return StreamlitAPPConfig()
