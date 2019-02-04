# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:28:38 2019

@author: Abhishek
"""

import cv2
import matplotlib.pyplot as plt

def main():
    window_name="Live Video Feed"
    cv2.namedWindow(window_name)
    cap=cv2.VideoCapture(0)
    
    print("Width :" + str(cap.get(3)))
    print("Height :" + str(cap.get(4)))
    
    cap.set(3,5000)
    cap.set(4,50 00)
    print("Width :" + str(cap.get(3)))
    print("Height :" + str(cap.get(4)))
    
    if cap.isOpened():
        ret,frame=cap.read()
    else:
        ret=False
    
    while ret:
        ret,frame=cap.read()
        output=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow(window_name,frame)
        cv2.imshow("Gray" ,output)
        
        if cv2.waitKey(1)==27:
            break
    cv2.destroyAllWindows()
    cap.release()
    
if __name__=="__main__":
    main()
        
    

