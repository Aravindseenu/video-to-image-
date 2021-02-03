import cv2
vidcap = cv2.VideoCapture('/home/nvidia/lanenet-lane-detection/data/tusimple_test_image/test2.mp4') #// enter the path to video file or give wewbcam as input
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 1 #//change this to required number of frames the video needs to be processed 
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
