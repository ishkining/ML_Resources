# thanks geeksforgeeks.org for example
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
from tensorflow.keras.applications import imagenet_utils
from IPython.display import Image

filename = 'content/birds.jpg'

Image(filename, width=224, height=224)
img = image.load_img(filename, target_size=(224, 224))
print(img)
plt.imshow(img)

model = tf.keras.applications.mobilenet_v2.MobileNetV2()
resize_dimg = image.img_to_array(img)
final_img = np.expand_dims(resize_dimg, axis=0)
final_img = tf.keras.applications.mobilenet_v2.preprocess_input(final_img)
final_img.shape
predictions = model.predict(final_img)

results = imagenet_utils.decode_predictions(predictions)
print(results)
