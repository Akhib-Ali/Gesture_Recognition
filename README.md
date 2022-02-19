# Gesture-Recognition
An opencv project for recognising the human gesture.


### AIM
To recognizes the human gestures seen in the camera frame and display the name of the gesture and controlling the light using human gesture.

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

![Screenshot from 2022-02-19 12-04-25](https://user-images.githubusercontent.com/86007193/154789627-77615ea5-2a16-4344-a276-7c3297517109.png)
2.Initialising and load model. <br />
For detecting the human gesture a model named mp_hand_gesture is used , which is a tensorflow pre defined model.
![Screenshot from 2022-02-19 12-09-17](https://user-images.githubusercontent.com/86007193/154789860-86478570-ed05-430f-b3e4-3458a426d88d.png)

![Screenshot from 2022-02-19 12-11-23](https://user-images.githubusercontent.com/86007193/154789952-9e5785b8-6887-4427-a2c9-5341d63338c9.png)

