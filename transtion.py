import cv2
import numpy as np

image =cv2.imread('ss/zzee.jpg')
cv2.imshow('Orimage',image)

row ,cols=image.shape[:2]


t_x=500
t_y=50



trans_materix=np.float32([[1,0,t_x],[0,1,t_y]])

trans_img=cv2.warpAffine(image,trans_materix,(cols,row))
cv2.imshow('Translation',trans_img)
cv2.waitKey(0)
cv2.destroyAllWindows()