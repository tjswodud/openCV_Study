import cv2

src = cv2.imread("D:\Image\LCKHighlight.PNG", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(src, 100, 255)

cv2.imshow("canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()