import cv2
import numpy as np
import face_recognition
import os

path = 'attandanceImages'
images =[]
names = []
listing = os.listdir(path)
print(listing)

for img in listing:
    currentImage = cv2.imread(f"{path}/{img}")
    images.append(currentImage)
    names.append(os.path.splitext(img)[0])
print(names)

image_glen = face_recognition.load_image_file("./basic_images/glen.jpg")
image_glen = cv2.cvtColor(image_glen, cv2.COLOR_BGR2RGB)

image_test = face_recognition.load_image_file("./basic_images/test_glen.jpg")
image_test = cv2.cvtColor(image_test, cv2.COLOR_BGR2RGB)

