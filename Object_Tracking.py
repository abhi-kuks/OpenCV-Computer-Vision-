# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:10:05 2019

@author: Abhishek
"""

import numpy as np
import cv2

def main():
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret,frame=cap.read()
    else:
        ret=False
    
    while ret:
        ret,frame=cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
        #blue Color
        low=np.array([100,50,50])
        high=np.array([140,255,255])
        
        #Greem Color
# =============================================================================
#         low=np.array([40,50,50])
#         high=np.array([80,255,255])
# =============================================================================
        
        #Red Color
# =============================================================================
#         low=np.array([140,50,0])
#         high=np.array([180,255,255])
# =============================================================================
        
        
        #Creating the Image Mask
        image_mask=cv2.inRange(hsv,low,high)
        output=cv2.bitwise_and(frame,frame,mask=image_mask)
        
        cv2.imshow("Original Video Feed",frame)
        cv2.imshow("Binary Image",image_mask)
        cv2.imshow("Object Tracking Feed",output)
        if cv2.waitKey(1)==27:
            break
    cv2.destroyAllWindows()
    cap.release()
if __name__=="__main__":
    main()











