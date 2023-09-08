import cv2

faceCascade = cv2.CascadeClassifier("D:\PycharmProjects\practice\Resources\haarcascades\haarcascades\haarcascade_frontalface_default.xml")
img = cv2.imread("D:\PycharmProjects\practice\Resources\lena.png")
#img = cv2.VideoCapture(0)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
print(faces)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)


cv2.imshow("Lena Image", img)

cv2.waitKey(0)