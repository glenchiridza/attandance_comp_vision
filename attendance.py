import cv2
import numpy as np
import face_recognition
import os

path = 'attandanceImages'
images = []
names = []
listing = os.listdir(path)
print(listing)

for img in listing:
    currentImage = cv2.imread(f"{path}/{img}")
    images.append(currentImage)
    names.append(os.path.splitext(img)[0])
print(names)


def find_encodings(image_list):
    encode_list = []
    for img in image_list:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoding = face_recognition.face_encodings(img)[0]
        encode_list.append(encoding)
    return encode_list


known_list_encoding = find_encodings(images)
print("process of encoding successful")

vid = cv2.VideoCapture(0)

while True:
    check, frame = vid.read()
    img = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    faces_frame_location = face_recognition.face_locations(img)
    encoding_faces_frame = face_recognition.face_encodings(img, faces_frame_location)

    for face_encode, face_locale in zip(encoding_faces_frame, faces_frame_location):
        matches = face_recognition.compare_faces(known_list_encoding, face_encode)
        face_distance = face_recognition.face_distance(known_list_encoding, face_encode)
        print(face_distance)
        match_index = np.argmin(face_distance)

        # display bounding box and write their name
        if matches[match_index]:
            name = names[match_index].title()
            print(name)

            y1, x2, y2, x1 = face_locale
            y1, x2, y2, x1 = y1 *4, x2 *4, y2 *4, x1 *4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)
            cv2.rectangle(frame, (x1, y2 - 25), (x2, y2), (0, 0, 0), cv2.FILLED)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255, 255), 2)

    cv2.imshow("cam_view", frame)
    cv2.waitKey(1)

# face_location = face_recognition.face_locations(img_glen)[0]
# glen_encoding = face_recognition.face_encodings(img_glen)[0]
# x, y, x2, y2 = face_location
# cv2.rectangle(img_glen, (x, y), (x2, y2), (255, 0, 255), 2)
#
# face_locat = face_recognition.face_locations(img_test)[0]
# test_encod = face_recognition.face_encodings(img_test)[0]
# x, y, x2, y2 = face_locat
# cv2.rectangle(img_test, (x, y), (x2, y2), (255, 0, 255), 2)
#
# results = face_recognition.compare_faces([glen_encoding], test_encod)
# face_distance = face_recognition.face_distance([glen_encoding], test_encod)
