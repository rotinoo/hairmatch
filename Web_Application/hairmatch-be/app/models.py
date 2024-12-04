from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array, load_img
import numpy as np

def load_models():
    face_shape_model = load_model('./model/male_face_shape_classifier.h5')
    hair_type_model = load_model('./model/hair_type_classifier.h5')
    face_classes = {0: "Oval", 1: "Rectangular", 2: "Round", 3: "Square"}
    hair_classes = {0: "Straight", 1: "Wavy", 2: "Curly", 3: "Dreadlocks", 4: "Kinky"}
    return face_shape_model, hair_type_model, face_classes, hair_classes

def predict_image(image_path, model, class_mapping, target_size=(224, 224)):
    image = load_img(image_path, target_size=target_size)
    image_array = img_to_array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    predictions = model.predict(image_array)
    predicted_index = np.argmax(predictions[0])
    return class_mapping[predicted_index]
