import cv2
import time

print("run")
img = cv2.imread("external-content.duckduckgo.com.jpg")

text = "Welcome to The YMCA Detector /nClick anywhere to begin!"

y_start = 100
y_inc = 550
x_start = 10
x_inc = 225
for i, line in enumerate(text.split("/n")):
    y = y_start + i * y_inc
    x = x_start + i * x_inc
    cv2.putText(img, line, (x, y), 2, 2.5, (0, 0, 255), 1, cv2.FONT_HERSHEY_DUPLEX)

cv2.imshow("Welcome Page", img)


def doYMCA(event, x, y, flags, params):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        img = cv2.rectangle(img, (0, 0), (1280, 720), (255, 255, 255), -1)
        textsize = cv2.getTextSize("Loading", cv2.FONT_HERSHEY_SIMPLEX, 4, 2)[0]
        img = cv2.putText(img, "Loading", (640 - (textsize[0]//2), 360 + (textsize[1]//2)), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 4, cv2.LINE_AA)
        cv2.imshow("Welcome Page", img)
        cv2.waitKey(1500)
        cv2.destroyAllWindows()
        
        exec(open("main.py").read()) 


# if left click down
cv2.setMouseCallback("Welcome Page", doYMCA)

cv2.waitKey(0)
cv2.destroyAllWindows()
