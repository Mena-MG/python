import cv2
image =cv2.imread('ss/noise.png')
# image =cv2.imread('ss/imgess.png')
#C:\Users\mena.magdy\Desktop\python\ss\immmjjj.webp
denosimge =cv2.medianBlur(image,5)
cv2.imshow('Orimage',image)
cv2.imshow(' DNimage',denosimge)
cv2.imwrite('imge123.png',denosimge)
cv2.waitKey(0)
cv2.destroyAllWindows()