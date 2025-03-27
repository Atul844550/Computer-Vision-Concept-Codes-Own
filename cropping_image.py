'''

import cv2
import numpy as np

image = cv2.imread("C:\\Users\\DELL\\computer Vision\\images\\person.jpg")

mask= np.float32([[1,0,200], [0,1,100]])

crop_image= cv2.warpAffine(image,mask, (500,500))      # used for cropping the image.

cv2.imshow("window", image)
cv2.imshow("window2", crop_image)
cv2.imshow("window3", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''


#----------------------cropping the image through slicing.-----------------------------------------------

import cv2
import numpy as np

image = cv2.imread("C:\\Users\\DELL\\computer Vision\\images\\person.jpg")

re_image= cv2.resize(image, (500,500))

 #  image[y1:y2, x1:x2]

crop_image= re_image[:200, 100:]

cv2.imshow("window", re_image)
cv2.imshow("window2", crop_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

