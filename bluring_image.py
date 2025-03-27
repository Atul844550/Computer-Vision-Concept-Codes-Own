import cv2
import numpy as np

image= cv2.imread("C:\\Users\DELL\\computer Vision\\images\\person.jpg")

re_image= cv2.resize(image, (300,300))

g= cv2.GaussianBlur(re_image, (7,7),0)
m= cv2.medianBlur(re_image, 5)
b= cv2.bilateralFilter(re_image, 9,75,70)

h= np.hstack((re_image,g,m,b))

cv2.imshow("image", h)
cv2.waitKey(0)
cv2.destroyAllWindows()