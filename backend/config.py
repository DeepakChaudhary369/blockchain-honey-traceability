import os

from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()


class Settings:

    APP_NAME = os.getenv(
        "APP_NAME",
        "Blockchain Honey Traceability Assurance Agent"
    )

    APP_ENV = os.getenv(
        "APP_ENV",
        "development"
    )

    API_KEY = os.getenv(
        "API_KEY",
        ""
    )


settings = Settings()