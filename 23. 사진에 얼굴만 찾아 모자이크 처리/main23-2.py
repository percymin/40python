import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

ff = np.fromfile(r'23. 사진에 얼굴만 찾아 모자이크 처리\샘플사진.jpg', np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED) 
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.2,5)
for (x,y,w,h) in faces:
    face_img = img[y:y+h, x:x+w]
    #탐지된 얼굴부분을 자른다
    face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.1, fy=0.1) 
    #이미지를 축소한다
    face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA) 
    #이미지 확대
    img[y:y+h, x:x+w] = face_img
    #자른 이미지를 축소 확대한 이미지로 대체한다

cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()