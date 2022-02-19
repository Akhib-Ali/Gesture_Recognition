import cv2
import mediapipe as mp
import time
from openhab import OpenHAB 

import tensorflow as tf
from tensorflow.keras.models import load_model

base_url = 'http://localhost:8080/rest'
openhab = OpenHAB(base_url)

item_name="3f_light1"
bathroom_light=openhab.get_item(item_name)
print(bathroom_light.state)

import numpy as np

# Load the gesture recognizer model


# Load class names
f = open('gesture.names.txt', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)

check_list=['Call me','Smile','Okay','Rock','Fist','Peace']
 
class handDetector():
	def __init__(self, mode=False, maxHands=1, detectionCon=0.75, trackCon=0.74):
		self.mode = mode
		self.maxHands = maxHands
		self.detectionCon = detectionCon
		self.trackCon = trackCon
		self.mpHands = mp.solutions.hands
		self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.detectionCon, self.trackCon)
		self.mpDraw = mp.solutions.drawing_utils
		self.model = load_model('mp_hand_gesture')
 
	def findHands(self,img,draw=True):
		imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		self.results = self.hands.process(imgRGB)
		#print(results.multi_hand_landmarks)
 
		if self.results.multi_hand_landmarks:
			for handLms in self.results.multi_hand_landmarks:
				if draw:
					self.mpDraw.draw_landmarks(img, handLms,self.mpHands.HAND_CONNECTIONS)
		return img
 
	def findPosition(self, img, handNo=0, draw=True):
 
		lmList = []
		if self.results.multi_hand_landmarks:
			myHand = self.results.multi_hand_landmarks[handNo]
			for id, lm in enumerate(myHand.landmark):
				# print(id, lm)
				h, w, c = img.shape
				cx, cy = int(lm.x * w), int(lm.y * h)
				# print(id, cx, cy)
				lmList.append([cx, cy])
				if draw:
					cv2.circle(img, (cx, cy), 3, (255, 0, 255), cv2.FILLED)
 
		return lmList




	def gesture_identification(self,landmarks,classNames):
		prediction = self.model.predict([landmarks])
		print(prediction)
		classID = np.argmax(prediction)
		print(classID)
		print(prediction[0][classID])
		className = classNames[classID].capitalize()
		print(className)
		return className

def main():
	pTime = 0
	cTime = 0
	cap = cv2.VideoCapture(0)
	detector = handDetector()
	while True:
		success, img = cap.read()
		img = detector.findHands(img)
		lmList = detector.findPosition(img)
		
		if len(lmList) != 0:
			className=detector.gesture_identification(lmList,classNames)

			print(className)
			if className=='Stop' or className=='Live long':
				bathroom_light=openhab.get_item(item_name)
				print(bathroom_light.state)
				if bathroom_light.state=='ON':
					#bathroom_light.off()
					print("of..................")
				else:
					print("already of and continue................................")
					cv2.putText(img, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
					cv2.imshow("Output",img)
					cv2.waitKey(1)
					continue
			if className=='Thumbs up':
						
				bathroom_light=openhab.get_item(item_name)
				print(bathroom_light.state)
				if bathroom_light.state=='OFF':
					#bathroom_light.on()
					print("on...........................................")
				else:
					print("already on and continue..................................")
					cv2.putText(img, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
					
					cv2.imshow("Output",img)
					continue

			cv2.putText(img, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
	
		# Show the final output
		
		cTime=time.time()
		fps=1/(cTime-pTime)
		pTime=cTime
		cv2.putText(img, f'FPS: {int(fps)}',(400,470),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),2)
		cv2.imshow("Output", img) 
		if(cv2.waitKey(1) & 0xFF== ord('q')):
			break



if __name__ == "__main__":
    main()



