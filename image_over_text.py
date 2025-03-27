import cv2
import numpy as np

image= cv2.imread("images/person.jpg")             
re_image= cv2.resize(image, (500,500)) 

text_image= cv2.putText(img = re_image, text=" Atul Soni", org= (10, 200), fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color= (0, 255,0), thickness=3, lineType= cv2.LINE_AA, bottomLeftOrigin=False )
text_image= cv2.putText(img = re_image, text=" Atul Soni", org= (10, 210), fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color= (0, 255,0), thickness=3, lineType= cv2.LINE_AA, bottomLeftOrigin=True )


cv2.imshow("window", re_image)
cv2.waitKey(0)
cv2.destroyAllWindows()