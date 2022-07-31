import cv2
import imutils
import dlib
import numpy as np
import tensorflow as tf
import time

from resources.config import settings
from utils.ekyc_utils import *
from dtos.face2vec_response_dto import FaceToVec


def encoder(image: np.ndarray):

  response = FaceToVec()

  image  = resize_image(image)
  faces = face_detect(image)
  if len(faces) == 0:
    response.set_error_response(400045)
  elif len(faces) != 1:
    response.set_error_response(400049)
  else:
    face = faces[0]
    x = face[0]
    y = face[1]
    w = face[2]
    h = face[3]
    frame = image[y:y+h, x:x+w]
    frame = cv2.resize(frame, (221, 221))
    frame = frame /255.
    frame = np.expand_dims(frame, axis=0)
    frames = [ frame, frame, frame ]
    emb = settings.model.predict(frames).tolist()
    response.set_succeed_response(
      200,
      emb[0]
    )
  return response
    
def setting_up():
  dlib.DLIB_USE_CUDA=True
  gpus = tf.config.experimental.list_physical_devices('GPU')
  if len(gpus) > 0:
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
      tf.config.set_logical_device_configuration(
        gpu,
        [tf.config.LogicalDeviceConfiguration(memory_limit=settings.vram_limit*1024)]
      )
  settings.model = load_retrain(gen_model())
