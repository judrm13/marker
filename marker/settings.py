
__version_info__ = (2, 1, 5)
__version__ = ".".join(map(str, __version_info__))
__author__ = "Mustafa Quraish"
__license__ = "MIT"


import os
from pydantic_settings import BaseSettings  # en lugar de pydantic.BaseSettings

class MarkerSettings(BaseSettings):
    log_level: str = os.getenv("MARKER_LOG_LEVEL", "INFO")

settings = MarkerSettings()

