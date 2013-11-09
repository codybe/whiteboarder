'''
Working Web-Cam in Python
'''

import cv2
import numpy as np

'''
Put Your Code in process
'''

def process(img):
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	circles =  cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1, 40, np.array([]), 100, 40, 5, 300)
	if circles is not None:
		for c in circles[0]:
			#Draw Circle
			cv2.circle(img, (c[0],c[1]), c[2], (100,255,100),2)
			#Draw enter
			cv2.circle(img, (c[0],c[1]), 1, (100,100 ,255),2)
	gray = np.float32(gray)
	dst = cv2.cornerHarris(gray,4,3,0.04)

	#result is dilated for marking the corners, not important
	dst = cv2.dilate(dst,None)

	# Threshold for an optimal value, it may vary depending on the image.
	img[dst>0.01*dst.max()]=[0,0,255]
	cv2.imshow("Image Feed",img)

def main():
	cv2.namedWindow("Image Feed")
	vc = cv2.VideoCapture(0)

	rval, frame = vc.read()

	while True:
		if frame is not None:
			#Show Live Image
			#cv2.imshow("preview", frame)
			#Process it instead
			process(frame)
  	
  		rval, frame = vc.read()

  		if cv2.waitKey(1) & 0xFF == ord('q'):
  			break

#Call Main
main()

