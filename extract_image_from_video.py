import cv2


video= cv2.VideoCapture("C:\\Users\\DELL\\computer Vision\\images\\metapreview.mp4")

c=0


while video.isOpened():
    r, frame=  video.read()
    if r==True:
        frame= cv2.resize(frame, (400,400))

        file_name= "C:\\Users\\DELL\\computer Vision\\images\\new_image_"+ str(c)+".png"
        new_image= cv2.imwrite(file_name, frame)
        cv2.imshow("window", frame)
        c=c+1
        if cv2.waitKey(25) & 0xff== ord("p"):                # here waitkey() is used for 1 bit per second
            break
    else:
        break

video.release()
cv2.destroyAllWindows()
         