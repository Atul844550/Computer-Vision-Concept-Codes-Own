import cv2
import numpy as np

def atul(x):
    pass

image= np.zeros((500,500,3), np.uint8)*255
cv2.namedWindow("color") # for naming the window


cv2.createTrackbar("R", "color", 0,255, atul)
cv2.createTrackbar("G", "color", 0,255, atul)
cv2.createTrackbar("B", "color", 0,255, atul)

while True:
    cv2.imshow("color", image)
    if cv2.waitKey(1) & 0xff== ord("p"):
        break
    r= cv2.getTrackbarPos("R", "color")
    g= cv2.getTrackbarPos("G", "color")
    b= cv2.getTrackbarPos("B", "color")

    image[:]= [b,g,r]

cv2.destroyAllWindows()
    



