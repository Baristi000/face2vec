from fastapi import FastAPI
import uvicorn
# from pyngrok import ngrok, conf
# import nest_asyncio

from api.__init__ import api_router
from resources.config import settings
from ai.ekyc import setting_up

app = FastAPI()
app.include_router(api_router)

@app.on_event("startup")
def init():
    setting_up()

@app.get("/")
def get_test():
    return "Hello from trieu ekyc"

if __name__ == "__main__":
#   conf.get_default().region = "ap"
#   ngrok.set_auth_token("22B0LQqb9sYGi73L8xXh8JNFZve_43sVjPz4KcVRbVKTANns8")
#   ngrok_tunnel = ngrok.connect(settings.port)
#   print('Public URL:', ngrok_tunnel.public_url)
#   nest_asyncio.apply()
#   uvicorn.run("__main__:app", host=settings.host, port=settings.port, reload=True, workers=10)
  uvicorn.run("__main__:app", host=settings.host, port=settings.port)
