import cv2
import datetime

capture = cv2.VideoCapture('D:\Image\FULL_LCKSpring2020_T1vsAF_W9D1_G2.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False

while True:
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("D:\Image\FULL_LCKSpring2020_T1vsAF_W9D1_G2.mp4")

    ret, frame = capture.read()
    cv2.imshow('VideoFrame', frame)

    now = datetime.datetime.now().strftime("%d_%H-%M-%S")
    key = cv2.waitKey(33)

    if key == 27:
        break
    elif key == 26:
        print('Capture')
        cv2.imwrite("D:/Image/Capture/" + str(now) + ".png", frame)
    elif key == 24:
        print("Start Recording")
        record = True
        video = cv2.VideoWriter("D:/Image/Video/" + str(now) + ".mp4", fourcc, 20.0, (frame.shape[1], frame.shape[0]))
    elif key == 3:
        print("Stop Recording")
        record = False
        video.release()

    if record == True:
        print("Recording...")
        video.write(frame)

capture.release()
cv2.destroyAllWindows()
