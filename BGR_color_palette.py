# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 22:28:01 2019

@author: Abhishek
"""

import cv2
import numpy as np

def empty_function():
    pass

def main():
    img=np.zeros((720,720,3),np.uint8)
    window_name="Opencv BGR Color Palette"
    cv2.namedWindow(window_name)
    cv2.createTrackbar("Blue",window_name,0,255,empty_function)
    cv2.createTrackbar("Green",window_name,0,255,empty_function)
    cv2.createTrackbar("Red",window_name,0,255,empty_function)
    
    
    while (True):
        cv2.imshow(window_name,img)
        if cv2.waitKey(1)==27:
            break
        blue=cv2.getTrackbarPos("Blue",window_name)
        green=cv2.getTrackbarPos("Green",window_name)
        red=cv2.getTrackbarPos("Red",window_name)
        
        img[:]=[blue,green,red]
        print(blue,green,red)
        
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()