import cv2
import numpy as np
import face_recognition

img_glen = face_recognition.load_image_file("./basic_images/glen.jpg")
img_glen = cv2.cvtColor(img_glen, cv2.COLOR_BGR2RGB)

img_test = face_recognition.load_image_file("./basic_images/wendy.jpeg")
img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)

# find faces in our image and encodings
face_location = face_recognition.face_locations(img_glen)[0]
glen_encoding = face_recognition.face_encodings(img_glen)[0]
x, y, x2, y2 = face_location
cv2.rectangle(img_glen, (x, y), (x2, y2), (255, 0, 255), 2)

face_locat = face_recognition.face_locations(img_test)[0]
test_encod = face_recognition.face_encodings(img_test)[0]
x, y, x2, y2 = face_locat
cv2.rectangle(img_test, (x, y), (x2, y2), (255, 0, 255), 2)

results = face_recognition.compare_faces([glen_encoding], test_encod)
face_distance = face_recognition.face_distance([glen_encoding], test_encod)
print(results, face_distance)
cv2.putText(img_test, f"{results} {round(face_distance[0],2)}", (50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow("glen chiridza", img_glen)
cv2.imshow("glen chiridza test image", img_test)
cv2.waitKey(0)

cv2.destroyAllWindows()
