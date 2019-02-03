# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:01:45 2019

@author: Abhishek
"""

import cv2
import matplotlib.pyplot as plt

def main():
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret,frame=cap.read()
    else:
        ret=False

    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    plt.imshow(img,cmap="Blues")
    plt.title('Color Image')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    
    cap.release()

if __name__=="__main__":
    main()

    



