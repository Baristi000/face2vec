from fastapi import APIRouter, UploadFile, File, Form

from utils.ekyc_utils import bytes_to_cv2
from ai.ekyc import encoder

router = APIRouter()

@router.post(
    "/encode",
    description="Vectorize"
)
async def encode(
  image: UploadFile = File(...)
  # name: str = Form(...)
):
  contents = await image.read()
  cs2_image = bytes_to_cv2(contents)
  emp = encoder(cs2_image)
  
  return {
      "data": emp
    }
