# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 12:14:03 2019

@author: Abhishek
"""


import cv2
import numpy as np


window_name="Drawing"
img=np.zeros((720,720,3),np.uint8)
cv2.namedWindow(window_name)

#Mouse Call back Function
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),50,(0,255,0),-1)
    if event==cv2.EVENT_MBUTTONDOWN:
        cv2.circle(img,(x,y),40,(0,0,255),-1)
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),30,(255,0,0),-1)        

#Bind the callback function to window
cv2.setMouseCallback(window_name,draw_circle)


def main():
    while(True):
        cv2.imshow(window_name,img)
        
        if cv2.waitKey(1)==27:
            break
    cv2.destroyAllWindows()
    

if __name__=="__main__":
    main()



