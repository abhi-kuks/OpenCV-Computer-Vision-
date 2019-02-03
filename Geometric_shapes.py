# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 10:04:48 2019

@author: Abhishek
"""

import cv2
import numpy as np

def main():
    img=np.zeros((720,720,3),np.uint8)
    cv2.line(img,(0,99),(99,0),(255,0,0),2)
    cv2.rectangle(img,(100,60),(200,170),(0,255,0),3)
    cv2.circle(img,(60,60),50,(0,0,255),-1)
    cv2.ellipse(img,(160,260),(50,20),0,0,360,(127,127,127),-1)
    points=np.array([[80,2],[125,5],[179,0],[230,5],[30,50]],np.int32)
    points=points.reshape(-1,1,2)
    cv2.polylines(img,[points],True,(0,255,255))
    text="Abhishek"
    cv2.putText(img,text,(100,100),cv2.FONT_HERSHEY_SIMPLEX,5,(255,255,0))
    cv2.imshow('Lena',img)
    cv2.waitKey(0)
    cv2.destroyWindow("Lena")
    
if __name__=="__main__":
    main()
    
    
    