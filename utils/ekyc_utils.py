from tensorflow.keras.models import Model
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import *
from tensorflow.keras import applications
from tensorflow.keras import backend as K
import tensorflow as tf
import cv2
import numpy as np

def gen_model():
    vgg_model = applications.VGG19(weights=None, include_top=False, input_shape=(221, 221, 3))
    x = vgg_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(4096, activation='relu')(x)
    x = Dropout(0.6)(x)
    x = Dense(4096, activation='relu')(x)
    x = Dropout(0.6)(x)
    x = Lambda(K.l2_normalize)(x)
    convnet_model = Model(inputs=vgg_model.input, outputs=x)

    first_input = Input(shape=(221,221,3))
    first_conv = Conv2D(96, kernel_size=(8,8), strides=(16,16), padding='same')(first_input)
    first_max = MaxPool2D(pool_size=(3,3), strides=(2,2), padding='same')(first_conv)
    first_max = Flatten()(first_max)
    first_max = Lambda(K.l2_normalize)(first_max)

    second_input = Input(shape=(221,221,3))
    second_conv = Conv2D(96, kernel_size=(8,8), strides=(32,32), padding='same')(second_input)
    second_max = MaxPool2D(pool_size=(7,7), strides=(4,4), padding='same')(second_conv)
    second_max = Flatten()(second_max)
    second_max = Lambda(K.l2_normalize)(second_max)
                        
    merge_one = concatenate([first_max, second_max])
    merge_two = concatenate([merge_one, convnet_model.output])
    emb = Dense(4096)(merge_two)
    emb = Dense(128)(emb)
    emb = tf.convert_to_tensor(emb, dtype='float32')
    l2_norm_final = Lambda(K.l2_normalize)(emb)

    model = Model(inputs=[first_input, second_input, convnet_model.input], outputs=l2_norm_final)
    return model

def load_retrain(model):
  model.load_weights("resources/triplet_weight.hdf5")
  return model

def bytes_to_cv2(data: bytes):
  nparr = np.fromstring(data, np.uint8)
  img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
  return img

