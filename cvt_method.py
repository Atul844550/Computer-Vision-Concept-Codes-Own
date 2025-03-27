import cv2

image= cv2.imread("C:\\Users\\DELL\\computer Vision\\images\\person.jpg")

re_image= cv2.resize(image, (400,400))

color_image= cv2.cvtColor(re_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("window", color_image)

cv2.waitKey(0)
cv2.destroyAllWindows()