import cv2
import numpy as np

image=cv2.imread("C:\\Users\\DELL\\computer Vision\\images\\person.jpg")

#creating whte image as a white board

white_image= np.ones((400,400, 3), np.uint8)*255

# create black image as a black board

black_image= np.zeros((500,500,3), np.uint8)*255


img= cv2.resize(image, (400,400))

#cv2.imshow("window", img)

cv2.imshow("window2", white_image)
cv2.imshow("window3", black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
