# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 12:26:54 2019

@author: Abhishek
"""

import matplotlib.pyplot as plt
import cv2
def main():
    path="G:\\Computer_Vision\\Images\\"
    
    imgpath1=path + "4.2.01.tiff"
    imgpath2=path + "Lena_color_256.tif"
    
    img1=cv2.imread(imgpath1,1)
    img2=cv2.imread(imgpath2,1)
    
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    
    plt.subplot(1,2,1)
    plt.imshow(img1)
    plt.title("Water Drop")
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1,2,2)
    plt.imshow(img2)
    plt.title("Lena Image")
    plt.xticks([])
    plt.yticks([])


    plt.show()

if __name__=="__main__":
    main()