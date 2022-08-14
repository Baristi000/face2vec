import cv2
import numpy as np
import imutils
import dlib
from arcface.ArcFace import ArcFaceModel

# Tạo model
def gen_model():
  return ArcFaceModel(size=112,
                      backbone_type="ResNet50",
                      training=False)

# Tải retrained model
def load_retrain(model):
  model.load_weights("resources/checkpoints/saved.ckpt")
  return model

# Chuyển đổi bytes sang numpy vector
def bytes_to_cv2(data: bytes):
  nparr = np.fromstring(data, np.uint8)
  img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
  return img

# resize ảnh về 800
def resize_image(image: np.ndarray):
  image = imutils.resize(image, width=800)
  return image

# Phát hiện khuôn mặt
def face_detect(image: np.ndarray):
  positions = []
  # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  hog_face_detector = dlib.get_frontal_face_detector()
  faces_hog = hog_face_detector(image, 1)
  if len(faces_hog) == 1:
    x = faces_hog[0].left()
    y = faces_hog[0].top()
    w = faces_hog[0].right() - x
    h = faces_hog[0].bottom() - y
    item = [x,y,w,h]
    positions.append(item)
  return positions
