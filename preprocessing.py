import cv2
import numpy as np

def preprocess_face(image, size=(128,128)):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, size)
    normalized = resized / 255.0
    return normalized
