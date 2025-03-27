import cv2

image= cv2.imread("C:\\Users\\DELL\\computer Vision\\images\\person.jpg")

re_image= cv2.resize(image, (500,500))

new = cv2.imwrite("new_image.png", re_image)

cv2.imshow("window", re_image)
cv2.waitKey(0)
cv2.destroyAllWindows()