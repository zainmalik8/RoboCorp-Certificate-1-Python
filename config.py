"""Configuration of bot."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class BotData:
    username: str = os.getenv("username")
    password: str = os.getenv("password")
    sales_file_url: str = os.getenv("file_url")
    output_path: str = f"{os.getcwd()}/output"
