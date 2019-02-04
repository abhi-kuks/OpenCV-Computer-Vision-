# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:53:01 2019

@author: Abhishek
"""

import cv2

def empty_function(x):
    pass


def main():
    path="G:\\Computer_Vision\\Images\\"
    imgpath1=path+'woman_darkhair.tif'
    imgpath2=path+'Lena_color_512.tif'
    
    img1=cv2.imread(imgpath1,1)
    img2=cv2.imread(imgpath2,1)
    
    output=cv2.addWeighted(img1,0.5,img2,0.5,0)
    
    window_name="Transition Demo"
    
    cv2.namedWindow(window_name)
    
    cv2.createTrackbar("Alpha",window_name,0,1000,empty_function)
    
    while(True):
        cv2.imshow(window_name,output)
        if cv2.waitKey(1)==27:
            break
        alpha=cv2.getTrackbarPos("Alpha",window_name)/1000
        beta=1-alpha
        output=cv2.addWeighted(img1,alpha,img2,beta,0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
    
    
    
    
    
    