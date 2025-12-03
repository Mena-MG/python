import cv2

import imutils

image =cv2.imread('ss/zzee.jpg')
cv2.imshow('Orimage',image)
h ,w = image.shape[:2]
Nw= int(w * 2)
Nh= int(h * 0.5)


scald_img = cv2.resize(image, (Nw,Nh))
cv2.imshow('Scaled',scald_img)
cv2.waitKey(0)
cv2.destroyAllWindows()