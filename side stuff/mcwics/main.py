import cv2
import mediapipe as mp
import numpy as np
import math
import functions
import threading

musicThread = threading.Thread(target=functions.playMusic)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

clicked = False
def click(event, x, y, flags, params):
  print("hi")
  if (event == cv2.EVENT_LBUTTONDOWN):
    global clicked
    if not clicked:
      clicked = True
    else:
      clicked = False

cap = cv2.VideoCapture(2)
curLetter = ""
prevLetter = ""
displayLetter = ""
position = (0, 0, 0, 0)
x = y = 0
isxyAssigned = False

currentYMCAPosition = 0

with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    print("Current position:", currentYMCAPosition)
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # print("right shoulder:", results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y)
    try:
        right_shoulder = np.array([results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y])
        left_shoulder = np.array([results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y])
        right_elbow = np.array([results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y])
        left_elbow = np.array([results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y])
        right_wrist = np.array([results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y])
        left_wrist = np.array([results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y])
        left_eye = np.array([results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE].y])
        right_eye = np.array([results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE].y])
        rightAngle = functions.getAngle(right_shoulder, right_elbow, right_wrist)
        leftAngle = functions.getAngle(left_shoulder, left_elbow, left_wrist)
        # print("rightAngle:", rightAngle, "leftAngle:", leftAngle, "wristDistance:", distance(right_wrist, left_wrist))

        if (functions.isY(right_wrist, left_wrist, right_elbow, left_elbow, right_shoulder, left_shoulder, right_eye, left_eye)):
            prevLetter = curLetter
            curLetter = "Y"
            displayLetter = "Y"
            currentYMCAPosition = 1
        elif (functions.isM(left_wrist, right_wrist, right_elbow, left_elbow, right_shoulder, left_shoulder, right_eye, left_eye)):
            if (curLetter != "M"):
                prevLetter = curLetter
                if (prevLetter == "Y"):
                    currentYMCAPosition = 2
                else:
                    currentYMCAPosition = 0
            curLetter = "M"
            displayLetter = "M"
        elif (functions.isC(right_wrist, left_wrist, right_eye, left_eye)):
            if (curLetter != "C"):
                prevLetter = curLetter
                if (prevLetter == "M" and currentYMCAPosition == 2):
                    currentYMCAPosition = 3
                else:
                    currentYMCAPosition = 0
            curLetter = "C"
            displayLetter = "C"
        elif (functions.isA(right_wrist, left_wrist, right_shoulder, left_shoulder, right_elbow, left_elbow)):
            if (curLetter != "A"):
                prevLetter = curLetter
                if (prevLetter == "C" and currentYMCAPosition == 3):
                    currentYMCAPosition = 4
                    musicThread.start()
                else:
                    currentYMCAPosition = 0
            curLetter = "A"
            displayLetter = "A"
        else:
            displayLetter = ""

    except:
      print("No pose detected")
      curLetter = ""

    textsize = cv2.getTextSize(displayLetter, cv2.FONT_HERSHEY_SIMPLEX, 4, 2)[0]
    
    if clicked:
      mp_drawing.draw_landmarks(
          image,
          results.pose_landmarks,
          mp_pose.POSE_CONNECTIONS,
          landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    
    image = cv2.flip(image, 1)

    image = cv2.putText(image, displayLetter, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), 2, cv2.LINE_AA)

    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('YMCA Detector', image)

    cv2.setMouseCallback('YMCA Detector', click, [clicked])

    x = (image.shape[1] - textsize[0])//2
    y = (image.shape[0] + textsize[1])//2
    if (not isxyAssigned):
      position = cv2.getWindowImageRect("YMCA Detector")
    
      isxyAssigned = True

    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()