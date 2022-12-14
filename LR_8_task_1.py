import cv2

# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("It`s me.jpg")
# DISPLAY
cv2.imshow("It`s me", img)
cv2.waitKey(0)
