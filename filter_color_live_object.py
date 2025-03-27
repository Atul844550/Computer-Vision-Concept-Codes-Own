import cv2
import numpy as np

video= cv2.VideoCapture(0)      # for camera opening 0 is used.

def fun(x):
    pass


cv2.namedWindow("color")
cv2.createTrackbar("lb", "color", 0,255, fun)
cv2.createTrackbar("lg", "color", 0,255, fun)
cv2.createTrackbar("lr", "color", 0,255, fun)

cv2.createTrackbar("ub", "color", 255,255, fun)
cv2.createTrackbar("ug", "color", 255,255, fun)
cv2.createTrackbar("ur", "color", 255,255, fun)

while video.isOpened():
    r, frame= video.read()

    if r==True:
        frame= cv2.resize(frame, (400,400))

        hsv_frame= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        Lb= cv2.getTrackbarPos("lb", "color")
        Lg= cv2.getTrackbarPos("lg", "color")
        Lr= cv2.getTrackbarPos("lr", "color")

        Ub= cv2.getTrackbarPos("ub", "color")
        Ug= cv2.getTrackbarPos("uG", "color")
        Ur= cv2.getTrackbarPos("ur", "color")

        lo= np.array([Lb, Lg, Lr])
        up= np.array([Ub, Ug, Ur])


        masks= cv2.inRange(hsv_frame, lo, up)

        res= cv2.bitwise_and(video, video, mask= masks)

        cv2.imshow("res", res)
        cv2.imshow("mask", masks)
        cv2.imshow("hsv", hsv_frame)
        cv2.imshow("video", video)

        if cv2.waitKey(1) & 0xff== ord("p"):
            break

    else:
        break

video.release()
cv2.destroyAllWindows()


