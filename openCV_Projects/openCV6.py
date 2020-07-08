import cv2

capture = cv2.VideoCapture("D:\Image\FULL_LCKSpring2020_T1vsAF_W9D1_G2.mp4")
templit = cv2.imread("D:\Image\minimap.png", cv2.IMREAD_GRAYSCALE)
dst = cv2.imread("D:\Image\LCKHighlight.PNG")

result = cv2.matchTemplate(capture, templit, cv2.TM_SQDIFF_NORMED)

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
x, y = minLoc
h, w = templit.shape

dst = cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 0, 255), 1)

'''
while True:
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("D:\Image\FULL_LCKSpring2020_T1vsAF_W9D1_G2.mp4")

    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    if cv2.waitKey(33) > 0:
        break
'''
# cv2.imshow("dst", dst)
# cv2.waitKey(0)
capture.release()
cv2.destroyAllWindows()