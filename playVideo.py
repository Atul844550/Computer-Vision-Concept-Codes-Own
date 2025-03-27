import cv2

video= cv2.VideoCapture("C:\\Users\\DELL\\computer Vision\\images\\metapreview.mp4")
#video= cv2.VideoCapture(0)       # 0 use for opening the camera

while video.isOpened():
    r, frame= video.read()
    if r == True:
        frame= cv2.resize(frame, (400,400))
        cv2.imshow("window", frame)

        if cv2.waitKey(20) & 0xff == ord("y"):
               break
    else:
         break

video.release()
cv2.destroyAllWindows()