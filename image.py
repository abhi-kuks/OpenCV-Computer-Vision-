# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2 
def main():
    imgpath="G:\\Computer_Vision\\Images\\4.1.01.tiff"
#     outpath="G:\\Computer_Vision\\abc.jpg"

    img=cv2.imread(imgpath,0)
    print(img)
    print(type(img))
    print(img.dtype)
    print(img.shape)
    print(img.ndim)
    print(img.size)
    
#     cv2.imwrite(outpath,img)
    cv2.namedWindow("Lena",cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Lena",img)
    cv2.waitKey(0)
    cv2.destroyWindow("Lena")    
     
if __name__=="__main__":
    main()


 






