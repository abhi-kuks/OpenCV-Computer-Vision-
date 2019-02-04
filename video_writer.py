# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:08:55 2019

@author: Abhishek
"""

import cv2

def main():
    window_name='Live Webcam Video Feed '
    cv2.namedWindow(window_name)
    cap=cv2.VideoCapture(0)
    filename="G:\\Computer_Vision\\Output\\output.avi"
    codec=cv2.VideoWriter_fourcc("W","M","V","2")
    framerate=30
    resolution=(640,480)
    video_file_output=cv2.VideoWriter(filename,codec,framerate,resolution)
    
    if cap.isOpened():
        ret,frame=cap.read()
    else:
        ret=False
    
    while ret:
        ret,frame=cap.read()
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_file_output.write(frame)
        cv2.imshow(window_name,frame)
        if cv2.waitKey(1)==27:
            break
    cv2.destroyAllWindows()
    cap.release()
    
if __name__=='__main__':
    main()
    





