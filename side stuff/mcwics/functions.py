import math
from playsound import playsound

def playMusic():
    playsound('ymca.mp3')

#Angle between points a and c, with midpoint being b
def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

#vertical distance between two points (over 0 if ideal is true, under 0 if ideal is false)
def verticalDistance(idealLower, idealUpper):
    return (idealLower[1] - idealUpper[1])

#horizontal distance between two points (over 0 if ideal is true, under 0 if ideal is false)
def horizontalDistance(idealLeft, idealRight):
    return (idealLeft[0] - idealRight[0])

#distance between two points
def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

#is the person doing a y shape?
#@params:
    #leftAngle: angle between left wrist and left shoulder
    #rightAngle: angle between right wrist and right shoulder
    #rightEyeToRightWrist: distance between right eye and right wrist
    #leftEyeToLeftWrist: distance between left eye and left wrist
    #wristDistance: distance between left wrist and right wrist
    #leftWristToElbow: distance between left wrist and left elbow
    #rightWristToElbow: distance between right wrist and right elbow
#@return: True if the person is doing a y shape, False otherwise
# def isY(leftAngle, rightAngle, rightEyeToRightWrist, leftEyeToLeftWrist, wristDistance, leftWristToElbow, rightWristToElbow):
def isY(rightWrist, leftWrist, rightElbow, leftElbow, rightShoulder, leftShoulder, rightEye, leftEye):
    
    wristToElbow = max(distance(leftWrist, leftElbow) * 0.8, distance(rightWrist, rightElbow) * 0.8)
    leftAngle = getAngle(leftShoulder, leftElbow, leftWrist)
    rightAngle = getAngle(rightShoulder, rightElbow, rightWrist)


    if (leftAngle > 100 and leftAngle < 180 and rightAngle > 180 and rightAngle < 250):
        if (distance(rightEye, rightWrist) > 0 and distance(leftEye, leftWrist) > 0):
            if (distance(leftWrist, rightWrist) > wristToElbow):
                if (not isM(leftWrist, rightWrist, rightElbow, leftElbow, rightShoulder, leftShoulder, rightEye, leftEye) and not isC(rightWrist, leftWrist, rightEye, leftEye)):
                    return True
    return False

#is the person doing an m shape?
#@params:
    #leftAngle: angle between left wrist and left shoulder
    #rightAngle: angle between right wrist and right shoulder
    #rightWristToShoulder: distance between right wrist and right shoulder
    #leftWristToShoulder: distance between left wrist and left shoulder
    #wristDistance: distance between left wrist and right wrist
    #leftWristToElbow: distance between left wrist and left elbow
    #rightWristToElbow: distance between right wrist and right elbow
#@return: True if the person is doing an m shape, False otherwise

def isM(leftWrist, rightWrist, rightElbow, leftElbow, rightShoulder, leftShoulder, rightEye, leftEye):
    # newWristToElbow = max(leftWristToElbow, rightWristToElbow)
    if (verticalDistance(rightShoulder, rightWrist) > 0 and verticalDistance(leftShoulder, leftWrist) > 0):
        leftAngle = getAngle(leftShoulder, leftElbow, leftWrist)
        rightAngle = getAngle(rightShoulder, rightElbow, rightWrist)
        if (rightAngle > 240 and leftAngle < 120):
            if (distance(leftWrist, leftEye) < (distance(leftEye, leftElbow) * 1.3) and distance(rightWrist, rightEye) < (distance(rightEye, rightElbow) * 1.3)):
                return True
    return False

def isC(rightWrist, leftWrist, rightEye, leftEye):
    vertBetweenWrists = abs(verticalDistance(rightWrist, leftWrist))
    if (vertBetweenWrists > 0.1):
        if((horizontalDistance(rightWrist, rightEye) > 0 and horizontalDistance(leftWrist, leftEye) > 0) or (horizontalDistance(rightWrist, rightEye) < 0 and horizontalDistance(leftWrist, leftEye) < 0)):
            return True
    return False
        
def isA(rightWrist, leftWrist, rightShoulder, leftShoulder, rightElbow, leftElbow):
    if (verticalDistance(rightShoulder, rightWrist) > 0 ) and (verticalDistance(leftShoulder, leftWrist) > 0):
        if (rightWrist[0] > rightShoulder[0] and leftWrist[0] < leftShoulder[0]):
            rightAngle = getAngle(rightShoulder, rightElbow, rightWrist)
            leftAngle = getAngle(leftShoulder, leftElbow, leftWrist)
            if (190 < rightAngle < 240 and 120 < leftAngle < 165):
                return True
    return False