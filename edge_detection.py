import cv2
import numpy as np

image= cv2.imread("C:\\Users\\DELL\\computer Vision\\images\\person.jpg")

re_image= cv2.resize(image, (500,500))

new_image= cv2.Canny(image= image, threshold1=7, threshold2= 7, apertureSize=7, L2gradient=False)

new_re_image= cv2.resize(new_image, (500,500))



cv2.imshow("image", re_image)
cv2.imshow("image2", new_re_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

