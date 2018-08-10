'''
AUTHOR: ceposerio@up.edu.ph
DESC: a demo of modifying and writing to a video file
'''
import cv2
import numpy as np

capture = cv2.VideoCapture("sample.avi")

if not capture.isOpened():
	capture.open()

# get width and height
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
dimension = (width,height)

# define video codec for file saving
fourcc = cv2.VideoWriter_fourcc('X','V','I','D') # four-char-code
# fourcc = cv2.VideoWriter_fourcc(*'XVID') # sequence decompression
frames_per_second = 20.0
out = cv2.VideoWriter('output.avi', fourcc, frames_per_second, dimension)

while True:
	ret, frame = capture.read()

	if ret:
		# we can modify the frame before display or write
		# simple binarization of the frame
		threshold = 68
		for i in range(height):
			for j in range(width):
				# get the average of BGR
				gray = sum(frame[i,j])/3
				# set to black if less than threshold; otherwise, white
				frame[i,j] = [0,0,0] if gray < threshold else [255,255,255]

		# Pythonic (better) way of doing the same stuff
		# mask = np.sum(frame,2)/3 < threshold
		# frame[mask] = [0,0,0]
		# mask = np.invert(mask)
		# frame[mask] = [255,255,255]
		
		cv2.imshow("Video", frame)
		out.write(frame) # write frame to file
	else:
		print("read failed")
		break
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

capture.release()
# release the opened file
out.release()
cv2.destroyAllWindows()