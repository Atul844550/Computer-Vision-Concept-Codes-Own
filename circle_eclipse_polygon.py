import cv2
import numpy as np

image= cv2.imread("images/person.jpg")             
re_image= cv2.resize(image, (500,500)) 

#cv2.circle(img= re_image, center=(250,250), radius=70,  color=(0,0,155), thickness=-1, lineType=cv2.FONT_HERSHEY_TRIPLEX)

#cv2.ellipse(img= re_image, center=(250,250), axes=(50,100),angle=30, startAngle=0,endAngle=360,   color=(0,0,155), thickness=2, lineType=cv2.FONT_HERSHEY_TRIPLEX)
new_poly=cv2.polylines(img= re_image, pts= [np.array([[100,400],[150,300],[300,400],[300,600],[100,400]])], isClosed=True, color=(255,0,0), thickness=3, lineType=4)



cv2.imshow("window", new_poly)
cv2.waitKey(0)
cv2.destroyAllWindows()