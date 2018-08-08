import cv2

capture = cv2.VideoCapture(0) # from default camera
# parameter can be a string, filename

# check if capture is initialized
if not capture.isOpened():
	capture.open()

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
	ret, frame = capture.read()

	if ret:
		# we can modify the frame before display
		# simple binarization of the frame
		# for i in range(height):
		# 	for j in range(width):
		# 		# get the average of BGR
		# 		gray = sum(frame[i,j])/3

		# 		frame[i,j] = [0,0,0] if gray < 100 else [255,255,255]
		cv2.imshow("Video", frame)
	else:
		print("read failed")
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# release the capture
capture.release()
cv2.destroyAllWindows()