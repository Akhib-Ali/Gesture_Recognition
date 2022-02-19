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
**1**. To  build this model we need to import the following. <br />

![Screenshot from 2022-02-19 12-04-25](https://user-images.githubusercontent.com/86007193/154789627-77615ea5-2a16-4344-a276-7c3297517109.png) <br />

**2**. Initialising and load model. <br />
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
#### Detecting Hand key points
For finding the hands and getting the landmarks of the hands a library called mediapipe is used. <br />
**mediapipe.solutions.hands**

If no hands are detected in the frame, then the length of the landmarks list will be 0, so we don’t need to do anything until a hand is detected.
If hands are detected, then we get the landmarks of the hand and the next step is to draw connections between the landmarks.
<br /> A sample skeleton of hand is shown below : <br />
![Screenshot from 2022-02-19 12-38-29](https://user-images.githubusercontent.com/86007193/154790888-33009043-9dcd-4b5b-8f4c-2454cc13f168.png) <br />

![Screenshot from 2022-02-19 16-15-21](https://user-images.githubusercontent.com/86007193/154797642-6dc008d6-524f-4d5b-bb3b-bf7cfd70276f.png) <br />
![Screenshot from 2022-02-19 16-15-38](https://user-images.githubusercontent.com/86007193/154797666-404193cb-1a9a-452f-a5bf-f4909f4dcbb3.png) <br />

  * MediaPipe works with RGB images but OpenCV reads images in BGR format. So, using cv2.cvtCOLOR() function  convert the     frame to RGB format.
  * The process function takes an RGB frame and returns a result class.
  * Then we check if any hand is detected or not, using result.multi_hand_landmarks method.
  * After that, we loop through each detection and store the coordinate on a list called landmarks.
  * Here image height (y) and image width(x) are multiplied with the result because the model returns a normalized result.       This means each value in the result is between 0 and 1.
  * And finally using mpDraw.draw_landmarks() function  draw all the landmarks in the frame.
#### Recognizing hand gesture
* Next step is to recognize the hand gesture using the tensorflow pre-defined model. 
* The model.predict() function takes a list of landmarks and returns an array contains 10 prediction classes for each landmark.<br />
The output looks like this- <br />
[[2.0691623e-18 1.9585415e-27 9.9990010e-01 9.7559416e-05
1.6617223e-06 1.0814080e-18 1.1070732e-27 4.4744065e-16 6.6466129e-07 4.9615162e-21]] <br />
![Screenshot from 2022-02-19 16-30-13](https://user-images.githubusercontent.com/86007193/154798178-5a061239-69e1-4e8d-b76d-1cd2016e3ded.png) <br />
* np.argmax() returns the index of the maximum value in the list.
* The list having the maximum value index is taken for identifying the gesture.
* After getting the index we can simply take the class name from the classNames list.
* Then using the cv2.putText function we show the detected gesture into the frame.
#### Openhab connection for light controlling using gesture
![Screenshot from 2022-02-19 16-49-59](https://user-images.githubusercontent.com/86007193/154798813-b80b4cbf-1db3-4eaf-84e1-d6baf40380a1.png)

* For controlling the lights we need to import Openhab library.
* Then fetch the item name or device that has been connected using openhab.
* Then, find the current state of the device [On or Off], this is for calling the on command if device is in off or vice versa.
* In this code the light will turn on when gesture recognised as **Thumbs up** and light will of when gesture recognised as **Stop**

### OUTPUT
<br /> ![Screenshot from 2022-02-19 16-48-38](https://user-images.githubusercontent.com/86007193/154798823-871d1b56-659c-4913-b1ea-ff95803fcfe4.png)
<br /> ![Screenshot from 2022-02-19 16-49-06](https://user-images.githubusercontent.com/86007193/154798843-6235fca0-9985-49a0-9b16-2284b04adce6.png)

**OUTPUT - Human Gesture Recognition**

![Screenshot from 2022-02-19 16-58-22](https://user-images.githubusercontent.com/86007193/154798963-8711728b-46b3-47bc-969c-f4c189855259.png)
![Screenshot from 2022-02-19 16-58-39](https://user-images.githubusercontent.com/86007193/154798990-ceabf14a-3134-452b-8906-e8d1c5b2c7c2.png)
![Screenshot from 2022-02-19 16-58-54](https://user-images.githubusercontent.com/86007193/154799001-cfce8cad-367d-41dd-a3db-af10551b5524.png)
![Screenshot from 2022-02-19 17-00-59](https://user-images.githubusercontent.com/86007193/154799039-b486e9c2-4a94-40e7-8780-54ab482cc5a3.png)
![Screenshot from 2022-02-19 17-01-14](https://user-images.githubusercontent.com/86007193/154799043-864efcb7-7c53-4369-bda5-918a803f7f04.png)
![Screenshot from 2022-02-19 17-01-22](https://user-images.githubusercontent.com/86007193/154799049-9cd41772-671e-4e10-a44c-9cbafac3dc22.png)
![Screenshot from 2022-02-19 17-03-32](https://user-images.githubusercontent.com/86007193/154799091-aa49bff4-51de-4100-afe5-b58f4c8803b7.png)

  


  


