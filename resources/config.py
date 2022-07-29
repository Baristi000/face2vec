from dotenv import load_dotenv
from os import *

class Setting():
  def __init__(self) -> None:
    load_dotenv(dotenv_path="resources/.env")
    self.host = getenv("HOST")
    self.port = int(getenv("PORT"))
    self.model = None
    self.vram_limit= int(getenv("VRAM_LIMIT"))

settings = Setting()