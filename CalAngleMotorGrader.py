import cv2
import os
import math
import numpy as np

os.chdir('B:/HCL/Catepillar/video/')
cap = cv2.VideoCapture('0601_Heavy_Blading_Soil.mp4')


while True:
    ret, img = cap.read()
    # print(img.shape) (360, 636, 3)
    # break
    img2 = img[0:180, 318:636]   # 60:110, 340:420
    #laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize =5)
    canny = cv2.Canny(img2, 100, 150, apertureSize = 3)

    lines = cv2.HoughLines(canny, 1, np.pi / 180, 50, min_theta = np.pi*4/5, max_theta = np.pi)
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
            cv2.line(img2, pt1, pt2, (0, 0, 255), 1)
    cv2.imshow('Original', cv2.resize(img, (800, 600)))
    cv2.imshow('Zoomin', cv2.resize(img2, (800, 600)))
    cv2.imshow('Canny', cv2.resize(canny, (800, 600)))

    if cv2.waitKey(25) & 0xFF == ord('q'):

        break

cap.release()
cv2.destroyAllWindows()


img = cv2.imread('B:/HCL/Catepillar/images/5600 Croped frame 288.jpg')
canny = cv2.Canny(img, 100, 150)
cv2.imshow('Canny', canny)


