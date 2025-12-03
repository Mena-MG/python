import cv2
image =cv2.imread('ss/zze.jpg')
cv2.imshow('Orimage',image)

alfa= 1#cont
beta100 =100#brit

adj=cv2.convertScaleAbs(image,alpha=alfa,beta=beta100)


cv2.imshow('Adjusted Image',adj)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()