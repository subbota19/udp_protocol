import cv2

#turn on camera
cap = cv2.VideoCapture(0)
# warm up the came that be photo will be more light
for i in range(30):
    cap.read()

#take a photo
ret, frame = cap.read()

# write to file(with png extension)
cv2.imwrite('photo.png', frame)

#turn off camera
cap.release()

