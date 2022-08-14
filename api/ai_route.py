from fastapi import APIRouter, UploadFile, File, Form

from utils.ekyc_utils import bytes_to_cv2
from ai.ekyc import encoder
from dtos.face2vec_response_dto import FaceToVec

router = APIRouter()

@router.post(
    "/encode",
    description="Vectorize",
    response_model=FaceToVec
)
async def encode(
  image: UploadFile = File(...)
):
  response = FaceToVec()
  try:
    contents = await image.read()
    cs2_image = bytes_to_cv2(contents)
    response = encoder(cs2_image)
  except Exception as e:
    print(e)
    response.set_error_response(500000)
  return response
  