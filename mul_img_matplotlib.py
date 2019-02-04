# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 11:35:12 2019

@author: Abhishek
"""

import matplotlib.pyplot as plt
import cv2
def main():
    path="G:\\Computer_Vision\\Images\\"
    
    imgpath1=path + "4.2.01.tiff"
    imgpath2=path + "Lena_color_256.tif"
    imgpath3=path + "woman_blonde.tif"    
    imgpath4=path + "4.1.04.tiff"
    
    img1=cv2.imread(imgpath1,1)
    img2=cv2.imread(imgpath2,1)
    img3=cv2.imread(imgpath3,1)
    img4=cv2.imread(imgpath4,1)
    
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    img3=cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)    
    img4=cv2.cvtColor(img4,cv2.COLOR_BGR2RGB)
    
    titles=["Water Drop","Lena","Blonde Woman","Woman"]
    images=[img1,img2,img3,img4]
    
    for i in range(4):
        
        plt.subplot(2,2,i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()

if __name__=="__main__":
    main()












