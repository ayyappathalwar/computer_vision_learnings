import cv2
import numpy as np

img = cv2.imread("D:\PycharmProjects\practice\Resources\WIN_20230624_17_13_59_Pro.jpg")
kernel = np.ones((5,5), np.uint8)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0)
imgcanny = cv2.Canny(img, 50, 100)
imgDilation = cv2.dilate(imgcanny,kernel, iterations=1)


while True:
    cv2.imshow("Gray_Image", imgGray)
    cv2.imshow("Blurred_Image", imgBlur)
    cv2.imshow("Edgecanned_Image", imgcanny)Chapter3

    cv2.imshow("Dilation_Image", imgDilation)
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break
