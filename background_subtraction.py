import cv2

original_video= cv2.VideoCapture("C:\\Users\\DELL\\computer Vision\\images\\metapreview.mp4")

subtract_obj= cv2.createBackgroundSubtractorMOG2()  # creating object for that method.

while original_video.isOpened():
    r, frame=  original_video.read()
    if r==True:
        frame= cv2.resize(frame, (500,500))
        sub_video= subtract_obj.apply(frame)   #now applying on the frame
        cv2.imshow("window", frame)
        cv2.imshow("window2", sub_video)

        if cv2.waitKey(20) & 0xff == ord("p"):
            break
    else:
        break

original_video.release()
cv2.destroyAllWindows()
