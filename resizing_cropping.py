import cv2
import numpy as np

img = cv2.imread("D:\PycharmProjects\practice\Resources\WIN_20230624_17_13_59_Pro.jpg")
print(img.shape)

imgresize = cv2.resize(img, (500,500))

imagecrop = img[100:600, 500:860]
while True:
    cv2.imshow("Image", img)
    cv2.imshow("Image1", imgresize)
    cv2.imshow("cropped image", imagecrop)
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break

