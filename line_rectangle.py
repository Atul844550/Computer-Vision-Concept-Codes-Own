import cv2
import numpy as np

image= cv2.imread("images/person.jpg")             
re_image= cv2.resize(image, (500,500)) 

cv2.rectangle(img= re_image, pt1= (70, 150), pt2=(70,250), color=(0,0,155), thickness=2, lineType=cv2.FONT_HERSHEY_TRIPLEX)
# cv2.rectangle(img= re_image, pt1= (70, 150), pt2=(250,250), color=(0,0,155), thickness=2, lineType=cv2.FONT_HERSHEY_TRIPLEX)


cv2.imshow("window", re_image)
cv2.waitKey(0)
cv2.destroyAllWindows()