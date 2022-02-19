# Gesture-Recognition
An opencv project for recognising the human gesture.


### AIM
To recognizes the human gestures seen in the camera frame and controlling the light using human gesture.

### REQUIREMENTS
*  opencv
*  Mediapipe
*  Tensorflow
*  Numpy
* openhab

### STEPS
1.Import necessary packages <br />
2.Initialize models <br />
3.Read frames from webcam <br />
4.Detect hand key points using mediapipe <br />
5.Recognize hand gestures using tensorflow <br />

### Implementation
1. To  build this model we need to import the following. <br />

![Screenshot from 2022-02-19 12-04-25](https://user-images.githubusercontent.com/86007193/154789627-77615ea5-2a16-4344-a276-7c3297517109.png) <br />
2.Initialising and load model. <br />
For detecting the human gesture a model named mp_hand_gesture is used , which is a tensorflow pre defined model. <br />
![Screenshot from 2022-02-19 12-09-17](https://user-images.githubusercontent.com/86007193/154789860-86478570-ed05-430f-b3e4-3458a426d88d.png) <br />
![Screenshot from 2022-02-19 12-11-23](https://user-images.githubusercontent.com/86007193/154789952-9e5785b8-6887-4427-a2c9-5341d63338c9.png) <br />
* Gesture.names file contains the name of the gesture classes. So first we open the file using python’s inbuilt open function and then read the file.After that, read the file using the read() function. <br />
Output: <br />
![Screenshot from 2022-02-19 12-27-50](https://user-images.githubusercontent.com/86007193/154790454-d5062ae0-c51b-402d-82f6-1e2d908f2830.png) <br />

* Read frames from the webcam <br />
![Screenshot from 2022-02-19 12-32-22](https://user-images.githubusercontent.com/86007193/154790654-180d2d50-384e-45a6-bd85-5c8f355ad0c2.png) <br />



* Create a VideoCapture object and pass an argument ‘0’. It is the camera ID of the system. 
* The cap.read() function reads each frame from the webcam.
* cv2.imshow() shows frames on a new openCV window.
* The cv2.waitKey() function keeps the display window open until the key ‘q’ is pressed.
#### Detect Hand key points
For finding the hands and getting the landmarks of the hands a library called mediapipe is used.
** mediapipe.solutions.hands **

If no hands are detected in the frame, then the length of the landmarks list will be 0, so we don’t need to do anything until a hand is detected.
If hands are detected, then we get the landmarks of the hand and the next step is to draw connections between the landmarks.
<br /> A sample skeleton of hand is shown below : <br />
![Screenshot from 2022-02-19 12-38-29](https://user-images.githubusercontent.com/86007193/154790888-33009043-9dcd-4b5b-8f4c-2454cc13f168.png) <br />



