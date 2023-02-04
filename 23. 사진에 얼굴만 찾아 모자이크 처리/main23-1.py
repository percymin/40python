import numpy as np
import cv2
# numpy, cv2 라이브러리를 불러온다

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
# 얼굴과 눈을 찾기위한 opencv 알고리즘이 적용된 파일을 불러옵니다

ff = np.fromfile(r'23. 사진에 얼굴만 찾아 모자이크 처리\샘플사진.jpg', np.uint8)
# opencv에서 한글경로의 파일을 읽지 못해 numpy로 파일을 읽어온다

img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
#incode하여 numpy의 이미지 파일을 opencv 이미지로 불러온다

img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)
#이미지의 크기를 조절한다

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#이미지에서 얼굴을 찾기위해 회색으로 설정

faces = face_cascade.detectMultiScale(gray, 1.2,5)
#여러개의 얼굴을 찾는다/ 1.2는 scalefactor(감도) , 5는 minNeighbor(최소 이격거리)을 나타낸다

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    # 얼굴을 찾아 파란색 네모처리해준다
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),(0,255,0),2)
    #눈을 찾아 초록 네모처리해준다

cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()