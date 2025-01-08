import cv2

cap = cv2.VideoCapture("../../Data/video_01.mp4")

color_1 = (0,0,255)
color_2 = (0,255,0)
line_width = 3
radius = 80
point_1 = (100,100)
point_2 = (400,100)
point_3 = (600,200)

fps = cap.get(cv2.CAP_PROP_FPS)
factor = 0.75
delay = int((1000 / fps) * factor)

while(True):
    ret, frame = cap.read()

    frame = cv2.resize(frame, (0,0), fx=1.5,fy=1.5)
    cv2.circle(frame, point_1, radius, color_1, line_width)
    cv2.rectangle(frame, point_2, point_3, color_2, line_width)

    cv2.imshow("Image", frame)
    cv2.moveWindow("Image", 0,0)

    ch = cv2.waitKey(delay)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

