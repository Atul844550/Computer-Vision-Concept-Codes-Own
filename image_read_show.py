import cv2
import numpy as np

image= cv2.imread("images/person.jpg")              # reading the image
re_image= cv2.resize(image, (200,200))              # resizing the image

h= np.hstack((re_image, re_image))                  # placing the images horizontally
v= np.vstack((h,h))                                 # placing the images vertically
cv2.imshow("first desktop image", v)                # showing the image on desktop window
cv2.waitKey(0)                                      # 0 pass for pressing any key it close the window or we can pass time also in milisec i.e 5000 for 5 sec
cv2.destroyAllWindows()                             # closing all windows


