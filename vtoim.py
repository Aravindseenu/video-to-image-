import cv2

# Opens the Video file
cap= cv2.VideoCapture('test2.mp4')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('Image'+str(i)+'.jpg',frame)#splits and writes every frame 
    i+=1

cap.release()
cv2.destroyAllWindows()