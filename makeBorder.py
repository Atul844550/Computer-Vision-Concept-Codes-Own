import cv2

image= cv2.imread("C:\\Users\\DELL\\computer Vision\\images\\person.jpg")

re_image= cv2.resize(image, (500,500))

new = cv2.copyMakeBorder(re_image,30, 30,30,30, cv2.BORDER_ISOLATED, None, value=255 )
new2 = cv2.copyMakeBorder(re_image,30, 30,30,30, cv2.BORDER_REFLECT101, None, value=255 )
new3 = cv2.copyMakeBorder(re_image,30, 30,30,30, cv2.BORDER_DEFAULT, None, value=255 )
new4 = cv2.copyMakeBorder(re_image,30, 30,30,30, cv2.BORDER_REPLICATE, None, value=255 )

cv2.imshow("window", new)
cv2.imshow("window2", new2)
cv2.imshow("window3", new3)
cv2.imshow("window4", new4)
cv2.waitKey(0)
cv2.destroyAllWindows()