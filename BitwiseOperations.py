import cv2 as cv
import numpy as np
import os

os.chdir('B:/Home/Picture/')
# Load two images
img1 = cv.imread('2015-12-22 124951.jpg')
img2 = cv.imread('Opencvwhite.png')
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[1224:(1224+rows), 500:(500+cols) ]
# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 150, 255, cv.THRESH_BINARY_INV)
mask_inv = cv.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg)

img1[1224:(1224+rows), 500:(500+cols) ] = dst
cv.imshow('res',cv.resize(img1, (800,600)))
cv.imshow('logo', img2)
cv.imshow('roi', roi)
cv.imshow('img_gray', img2gray)
cv.imshow('mask', mask)
cv.imshow('mask_inv', mask_inv)
cv.imshow('img1.bg', img1_bg)
cv.imshow('img2.fg', img2_fg)
cv.waitKey(0)
cv.destroyAllWindows()