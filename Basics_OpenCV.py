import cv2

img= cv2.imread ("D:\Illustrator\self\portrait.jpg", 1)
resized= cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("portrait", resized)
cv2.waitKey(5000)

cv2.destroyAllWindows()
