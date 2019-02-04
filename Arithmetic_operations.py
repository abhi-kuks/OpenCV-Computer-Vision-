# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 16:09:57 2019

@author: Abhishek
"""



import matplotlib.pyplot as plt
import cv2
def main():
    path="G:\\Computer_Vision\\Images\\"
    
    imgpath1=path + "4.2.01.tiff"
    imgpath2=path + "Lena_color_512.tif"

    
    img1=cv2.imread(imgpath1,1)
    img2=cv2.imread(imgpath2,1)
    
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    
    add=img1 + img2
    sub=img1 - img2
    mult=img1 * img2
    div=img1/img2    
    
    titles=["Water Drop","Lena","addition","subtraction","Multiplication","Division"]
    images=[img1,img2,add,sub,mult,div]
    
    for i in range(6):
        
        plt.subplot(1,6,i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()

if __name__=="__main__":
    main()



