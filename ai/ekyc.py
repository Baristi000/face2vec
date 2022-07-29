import cv2
import imutils
import dlib
import numpy as np
import tensorflow as tf

from resources.config import settings
from utils.ekyc_utils import *
import time

def encoder(image: np.ndarray):
  t = time.time()
  frames = []
  image = imutils.resize(image, width=800)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  hog_face_detector = dlib.get_frontal_face_detector()
  faces_hog = hog_face_detector(image, 1)
  if len(faces_hog) == 1:
    x = faces_hog[0].left()
    y = faces_hog[0].top()
    w = faces_hog[0].right() - x
    h = faces_hog[0].bottom() - y
    frame = image[y:y+h, x:x+w]
    frame = cv2.resize(frame, (221, 221))
    frame = frame /255.
    frame = np.expand_dims(frame, axis=0)
    frames = [ frame, frame, frame ]
  print("dlib process:", time.time()-t, "seconds")
  t = time.time()
  emb128 = settings.model.predict(frames).tolist()
  print("model process:", time.time()-t, "seconds")
  return emb128

def setting_up():
  dlib.DLIB_USE_CUDA=True
  settings.model = load_retrain(gen_model())
  gpus = tf.config.experimental.list_physical_devices('GPU')
  if len(gpus) > 0:
    for gpu in gpus:
      tf.config.set_logical_device_configuration(
        gpu,
        [tf.config.LogicalDeviceConfiguration(memory_limit=settings.vram_limit)]
      )
