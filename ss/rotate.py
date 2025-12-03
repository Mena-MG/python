import cv2

import imutils

image =cv2.imread('ss/zzee.jpg')
cv2.imshow('Orimage',image)
cv2.waitKey(0)

rotated= imutils.rotate(image,180)
cv2.imshow('Rotated',rotated)
cv2.waitKey(0)