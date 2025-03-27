import cv2
import numpy as np

image= cv2.imread("C:\\Users\DELL\\computer Vision\\images\\person.jpg")

re_image= cv2.resize(image, (400,400))
print(re_image.shape)

width, height= re_image.shape[0], re_image.shape[1]

m= cv2.getRotationMatrix2D((width/2, height/2), 270, 1)
rotate_image= cv2.warpAffine(re_image, m, (height, width) )          # it is used for cropping the image.

h= np.hstack((re_image, rotate_image))

cv2.imshow("image", h)
cv2.waitKey(0)
cv2.destroyAllWindows()