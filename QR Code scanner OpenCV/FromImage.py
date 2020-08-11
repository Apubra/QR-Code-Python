import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

image = cv2.imread("/home/apubra/Code/GitHub/QR-Code-Python/myQR.png")


decodedObjects = pyzbar.decode(image)
for obj in decodedObjects:
    print("Type:", obj.type)
    print("Data in bytes: ", obj.data, "\n")
    print("Data in String: ", obj.data.decode('utf-8'), "\n")

cv2.imshow("Frame", image)
cv2.waitKey(0)