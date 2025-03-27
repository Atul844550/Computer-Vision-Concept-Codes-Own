import cv2
import numpy as np
import os



list_name= os.listdir("C:\\Users\\DELL\\computer Vision\\images")
print(list_name)


for name in list_name:
    path = "C:\\Users\\DELL\\computer Vision\\images"
    image= path+"\\"+ name
    image= cv2.imread(image)  
    re_image= cv2.resize(image, (500,600))
    cv2.imshow("first desktop image", re_image)
    cv2.waitKey(2000)
cv2.destroyAllWindows()



                           