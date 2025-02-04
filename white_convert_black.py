from cv2 import cv2
img = cv2.imread("haber4.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

img[thresh == 255] = 0

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
erosion = cv2.erode(img, kernel, iterations = 1)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow("image", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()