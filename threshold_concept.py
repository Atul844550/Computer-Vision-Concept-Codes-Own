import cv2
import matplotlib.pyplot as plt

image= cv2.imread("C:\\Users\\DELL\\computer Vision\\images\\person.jpg")

image= cv2.resize(image, (400,400))

#b, threshold_image= cv2.threshold(image, 174,189,cv2.THRESH_BINARY)

hist= cv2.calcHist([image], [0], None, [255], [0,255])

_, ostu_image= cv2.threshold(image,0,255, (cv2.THRESH_BINARY+cv2.THRESH_OTSU))

plt.plot(hist)
plt.show()




#cv2.imshow("original image", image)
#cv2.imshow("threshold image", threshold_image)
cv2.imshow("window", ostu_image)
cv2.waitKey(0)
cv2.destroyAllWindows()