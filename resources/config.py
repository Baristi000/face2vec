from dotenv import load_dotenv
from os import getenv
import json

class Setting():
  def __init__(self) -> None:
    load_dotenv(dotenv_path="resources/.env")
    self.host = getenv("HOST")
    self.port = int(getenv("PORT"))
    self.model = None
    self.vram_limit = int(getenv("VRAM_LIMIT"))
    json_file = open('resources/response_code.json')
    self.response_code = json.load(json_file)
    json_file.close()

settings = Setting()