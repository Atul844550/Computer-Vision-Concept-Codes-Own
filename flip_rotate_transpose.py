import cv2

image=  cv2.imread("C:\\Users\\DELL\\computer Vision\\images\\person.jpg")

flip_image= cv2.flip(image, 0)       # x axis
flip_image2= cv2.flip(image, 1)       #y axis
flip_image3= cv2.flip(image, -1)       #x, y axis

rotate_image= cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)        # for rotation

transpose_image= cv2.transpose(image)                            # for transpose


#cv2.imshow("flip image 3", flip_image3)
#cv2.imshow("flip image 2", flip_image2)
#cv2.imshow("window", image)
#cv2.imshow("flip image", flip_image)

#cv2.imshow("window", rotate_image)

cv2.imshow("window", transpose_image)
cv2.waitKey(0)
cv2.destroyAllWindows()