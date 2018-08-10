'''
AUTHOR: ceposerio@up.edu.ph
DESC: a demo of opening and displaying a video file
'''
import cv2

capture = cv2.VideoCapture(0) # from default camera
# parameter can be a string, filename

# check if capture is initialized
if not capture.isOpened():
	capture.open()

while True:
	ret, frame = capture.read()
	# ret is a boolean that indicates if a frame was 
	# successfully read
	if ret:
		cv2.imshow("Video", frame)
	else:
		print("read failed")
		break
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# release the capture
capture.release()
cv2.destroyAllWindows()