import random
import serial
import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO


model = YOLO('best.pt')


def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)


cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap = cv2.VideoCapture(0)


my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")
# print(class_list)
count = 0

ser = serial.Serial('COM5', 9600, timeout=1)


while True:
    ret, frame = cap.read()
    count += 1
    # print(count)
    if count % 3 != 0:
        continue

    frame = cv2.resize(frame, (1020, 500))
    # x = random.randint(0, 50)
    # cv2.putText(frame,'Frame per second : ', x,(50, 50),font, 1,(0, 255, 255),2,cv2.LINE_4)
    results = model.predict(frame)

    # Get the object count
    # object_count = len(results.pandas().iloc[0])

    # # Print the object count
    # print("Object count:", object_count)

    # serial for arduino data passing

    # print("Res",results)
    a = results[0].boxes.boxes
    px = pd.DataFrame(a).astype("float")
    # print("PX",len(px))
    object_count = len(px)

    print("object count : ", object_count)

    # Send a signal to the Arduino to change the traffic light based on the object count
    if object_count > 0 and object_count <= 2:
        ser.write(b'1')  # Turn on the red light
    elif object_count == 3:
        ser.write(b'2')  # Turn on the yellow light
    elif object_count > 3:
        ser.write(b'3')  # Turn on the green light

    # Send the object count to Arduino Uno
    # ser.write(str(object_count).encode())

    # ser.close()
    # if cond
    for index, row in px.iterrows():
        #        print(row)

        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        # c=class_list[d]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, "Car", (x1, y1),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

ser.close()
cap.release()
cv2.destroyAllWindows()
