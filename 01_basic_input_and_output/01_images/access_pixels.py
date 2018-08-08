'''
AUTHOR: ceposerio@up.edu.ph
DESC: a demo of accessing and modifying pixels
'''
import cv2

# simple function to translate channel index to
# channel color name
def channel(x):
	if x == 0: return "B"
	if x == 1: return "G"
	if x == 2: return "R"
	return "X"


filename = "lena.jpg"
image = cv2.imread(filename)

# image properties
rows,cols,channels = image.shape
print("The image loaded has {} rows and {} columns.".format(rows,cols))
print("Also, the image has {}".format(channels))
print("There are {} pixels in the image".format(image.size))
print("Image data type is {}".format(image.dtype))

print(type(image))

# access each pixel using coordinates
for i in range(rows):
	for j in range(cols):
		pass
		# print("[B,G,R] {}".format(image[i,j]))
		# can access each channel in each pixel
		# by further adding a third component
		# e.g. image[i,j,0] to access the B channel
		# warning: accessing pixels individually costs lotsa resources

# pixels can be modified in the same way we accessed it
# e.g. set corner pixels to green
image[0,0] = [0,255,0]
image[0,cols-1] = [0,255,0]
image[rows-1,0] = [0,255,0]
image[rows-1,cols-1] = [0,255,0]

# access and modifying using slices
# corner = image[0:50, 0:50]
# image[50:100, 50:100] = corner

# let's show the image
windowName = "Hello OpenCV"
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

cv2.imshow(windowName, image)
keypressed = cv2.waitKey(0)

cv2.destroyAllWindows()