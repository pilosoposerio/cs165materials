'''
AUTHOR: ceposerio@up.edu.ph
DESC: a demo of creating image files
'''
import cv2

filename = "lena.jpg"
colorType = 0 # gray scale
image = cv2.imread(filename, colorType)

windowName = "Hello OpenCV"
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

cv2.imshow(windowName, image)
keypressed = cv2.waitKey(0) 

# write grayscaled image to a new file
filename2 = "lena-grayscale.png"
cv2.imwrite(filename2, image)
# type of image file created depends on file extension

cv2.destroyAllWindows()