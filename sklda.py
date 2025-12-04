import numpy as np
import cv2
import imutils

imge =np.ones((500,500,3),dtype=np.uint8)*255
# line
start = (400,400)
end = (100,100)
color = (0,255,0)
# line2
start2 = (400,300)
end2 = (100,300)
color2 = (0,255,0)

# circle
center = (200,200)
radius = 50
color = (0,255,0)
thinkness=5


# rectangle
startrect = (100,100)
endrect = (400,400)
color = (0,255,0)
thinkness=5

cv2.line(imge,start,end,color,thinkness)
cv2.line(imge,start2,end2,color2,thinkness)
# cv2.circle(imge,center,radius,color,thinkness)
cv2.rectangle(imge,startrect,endrect,color,thinkness)
# cv2.putText(imge,"Hello",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,color,thinkness)

# edited_imge = cv2.resize(imge,None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)

# rotated_image = imutils.rotate(edited_imge, 45)
# rotated_image = cv2.rotate(edited_imge, cv2.ROTATE_65)
# cv2.imshow("editd",edited_imge)
cv2.imshow("image",imge)
cv2.waitKey(0)
cv2.destroyAllWindows()
