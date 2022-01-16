import cv2

print("run")
img = cv2.imread("external-content.duckduckgo.com.jpg")

text = "Welcome to The YMCA Detector /nby The Village People!"

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
    print("hi")
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.destroyAllWindows()
        # imgCopy = img.copy()
        # cv2.imshow("Y", imgCopy)
        #insert script name to execute
        exec(open("main.py").read())


# if left click down
cv2.setMouseCallback("Welcome Page", doYMCA)

cv2.waitKey(0)
cv2.destroyAllWindows()
