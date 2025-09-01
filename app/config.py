from pathlib import Path

from dataclasses import dataclass
from dotenv import load_dotenv
import yaml

# load .env
load_dotenv()

@dataclass
class Paths:
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    SECRETS_PATH: Path = BASE_DIR.joinpath("app", "secrets.yml")

with open(Paths.SECRETS_PATH, "r", encoding="utf-8") as file:
    SECRETS = yaml.safe_load(file)