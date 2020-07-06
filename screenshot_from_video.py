# opencv python3 olarak ayarlı! update-alternatives --install /usr/bin/python python /usr/bin/python3.7 2
from cv2 import cv2 # pip3 install opencv-python
import os
import time

# Read the video from specified path
cam = cv2.VideoCapture("videoAndSound/haber_1_besiktas.mp4")

try:
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')
    # if not created then raise error
except OSError:
    print('Error: Creating directory of data')





# frame
currentframe = 0
frameSayisi = 2
frame_per_second = cam.get(cv2.CAP_PROP_FPS) 
for i in range(frameSayisi):
    # reading from frame
    ret, frame = cam.read()
    
    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)
        #if currentframe == (3*frame_per_second):  
        #    cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break
    
    time.sleep(30) # take schreenshot every 5 seconds

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()