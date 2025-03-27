import cv2

image= cv2.imread("C:\\Users\\DELL\\computer Vision\\images\\person.jpg")

new = cv2.pyrDown(image )

new2=cv2.pyrDown(new)

cv2.imshow("window", image)
cv2.imshow("window1", new)
cv2.imshow("window2", new2)

print(image.shape)
print(new.shape)
print(new2.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()