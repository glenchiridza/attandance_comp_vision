import cv2
import numpy as np
import face_recognition
import os

path = 'attandanceImages'
images =[]
names = []

image_glen = face_recognition.load_image_file("./basic_images/glen.jpg")
image_glen = cv2.cvtColor(image_glen, cv2.BRG2RGB)

image_test = face_recognition.load_image_file("./basic_images/test_glen.jpg")
image_test = cv2.cvtColor(image_test, cv2.BRG2RGB)

