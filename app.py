import cv2
import numpy as np
import face_recognition

img_glen = face_recognition.load_image_file("./basic_images/glen.jpg")
img_glen = cv2.cvtColor(img_glen, cv2.COLOR_BGR2GRAY)

img_test = face_recognition.load_image_file("./basic_images/test_glen.jpg")
img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2GRAY)


cv2.imshow("glen chiridza", img_glen)
cv2.waitKey(0)
