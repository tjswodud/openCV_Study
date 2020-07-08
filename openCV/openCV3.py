import cv2

video = cv2.VideoCapture("D:/Image/FULL_LCKSpring2020_T1vsAF_W9D1_G2.mp4")

gray = cv2.cvtColor(video, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

for i in range(len(contours)):
    cv2.drawContours(video, [contours[i]], 0, (0, 0, 255), 2)
    cv2.putText(video, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
    print(i, hierarchy[0][i])
    cv2.imshow("src", video)
    cv2.waitKey(0)

cv2.destroyAllWindows()
