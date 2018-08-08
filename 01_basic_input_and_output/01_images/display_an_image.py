'''
AUTHOR: ceposerio@up.edu.ph
DESC: a demo of opening and displaying an image
'''

# import opencv python library
import cv2


# open the image
filename = "lena.jpg"
image = cv2.imread(filename)
# type of image file loaded depends on file contents
# print(image) # what kind of object is it????

# create a window for displaying image
windowName = "Hello OpenCV"
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

# display the image
cv2.imshow(windowName, image)
keypressed = cv2.waitKey(0) # required after imshow()

# close all windows
cv2.destroyAllWindows()