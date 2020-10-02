import cv2
import keyboard



cap = cv2.VideoCapture(0)

#define the tracker  / we need to instal the package opencv-contrib
tracker = cv2.TrackerMOSSE_create()

#to initialize our tracker we need to read an image from our webcam so we can select the object
success, img = cap.read()

#select the initial bounding box of the object
bbox = cv2.selectROI("Tracking", img, False)

#initialize
tracker.init(img, bbox)


def drawBox(img, bbox):

    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    #draw a rectangle
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 1)

    cv2.putText(img, "Tracking", (10, 40), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 255, 0), 2, 1)

while True:

    timer = cv2.getTickCount()

    success, img = cap.read()

    #get the updated position of the object
    success, bbox = tracker.update(img)

    # if it finds the object, draw the bbox around the object, else return object lost
    if success is True:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "Object lost", (10, 40), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 0, 255), 2, 1)

    #put the fps on the display
    fps = cv2.getTickFrequency()/(cv2.getTickCount() - timer)
    cv2.putText(img, str(int(fps)), (10, 20), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 255, 255), 2)

    #display
    cv2.imshow('Tracking2', img)

    if cv2.waitKey(1) & keyboard.is_pressed('q'):  # pressing q will quit the display
        break

