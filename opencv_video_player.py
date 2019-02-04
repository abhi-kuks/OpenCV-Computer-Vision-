# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 21:12:57 2019

@author: Abhishek
"""

import cv2
def main():
    window_name="cv2 media player"
    cv2.namedWindow(window_name)
    filename="G:\\Computer_Vision\\Output\\abc.avi"
    cap=cv2.VideoCapture(filename)

    while (cap.isOpened()):
        ret,frame=cap.read()
        print(ret)
        if ret:
            cv2.imshow(window_name,frame)        
            if cv2.waitKey(33)==27:
                break
    cv2.destroyAllWindows()
    cap.release()

if __name__=='__main__':
    main()
    
        
    