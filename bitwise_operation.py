import cv2
import numpy as np

image1= cv2.imread("C:\\Users\\DELL\\computer Vision\\images\\facebook.png")
image2= cv2.imread("C:\\Users\\DELL\\computer Vision\\images\\instagram.jpg")
re_image1= cv2.resize(image1, (300,300))
re_image2= cv2.resize(image2, (300,300))

new_imge_and= cv2.bitwise_and(re_image1, re_image2)
new_imge_or= cv2.bitwise_or(re_image1, re_image2)
new_imge_xor= cv2.bitwise_xor(re_image1, re_image2)
new_imge_not= cv2.bitwise_not(re_image1, re_image2)



h= np.hstack((new_imge_and, new_imge_or, new_imge_not, new_imge_xor))

#cv2.imshow("image1", new_imge_and)
#cv2.imshow("image2", new_imge_or)
#cv2.imshow("image3", new_imge_xor)
#cv2.imshow("image4", new_imge_not)
cv2.imshow("image", h)
cv2.waitKey(0)
cv2.destroyAllWindows()