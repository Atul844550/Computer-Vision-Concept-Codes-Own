import cv2
import numpy as np

img1= cv2.imread("C:\\Users\\DELL\\computer Vision\\images\\facebook.png")
img2= cv2.imread("C:\\Users\\DELL\\computer Vision\\images\\instagram.jpg")

re_img1= cv2.resize(img1, (500,500))
re_img2= cv2.resize(img2, (500,500))

#cv2.imshow("img1", re_img1)
#cv2.imshow("img2", re_img2)

new_image_add= cv2.addWeighted(re_img1, 2,re_img2, 0, 1)

new_image_subtract= cv2.subtract(re_img1,re_img2, 2)

#cv2.imshow("new image", new_image_add)
cv2.imshow("new image2", new_image_subtract)




cv2.waitKey(0)
cv2.destroyAllWindows()