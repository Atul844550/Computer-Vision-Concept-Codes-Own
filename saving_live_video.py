import cv2


video= cv2.VideoCapture(0)

f= cv2.VideoWriter_fourcc(*"XVID")     # video codec (XVID is widely supported)
out= cv2.VideoWriter("demo.mp4", f, 40,0, (640,480), 0)

while video.isOpened():
    r, frame= video.read()

    if r==True:
        frame= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame= cv2.flip(frame, 1)  #flipping over the vertical axis.
        out.write(frame)
        cv2.imshow("window", frame)
        

        if cv2.waitKey(1) & 0xff==ord("p"):
            break
    else:
        break

video.release()
out.release()
cv2.destroyAllWindows()
