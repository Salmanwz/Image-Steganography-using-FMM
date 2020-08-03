from ImageRead import *
import sys
import numpy
import math
import cv2#Library for computer visions
class ImageEncrypting:
    def __init__(self):
        pass
    
    #Convert image array to modulus of five
    def makeModuleFiveImage(self,imgNpArray):
        imageRow,imageColumn=imgNpArray.shape[0],imgNpArray.shape[1]
        for row in range(0,imageRow):
            for col in range(0,imageColumn):
                if imgNpArray[row][col] % 5 == 4:
                    imgNpArray[row][col]+=1 
                elif imgNpArray[row][col] % 5 == 3:
                    imgNpArray[row][col]+=2 
                elif imgNpArray[row][col] % 5 == 2:
                    imgNpArray[row][col]-=2 
                elif imgNpArray[row][col] % 5 == 1: 
                    imgNpArray[row][col]-=1
    #Method to encrypt the message using the five modulous method
    def encryptMessage(self,imgNpArray,message):
        windowRowSize=6
        windowColSize=6
        imageRow,imageColumn=imgNpArray.shape[0],imgNpArray.shape[1]
        colStart=0
        rowStart=0
        for char in message:
            posCount=-1
            ASCII=ord(char)
            if ASCII%36==0:
                loopNumber=(ASCII//36)+1
            else:
                loopNumber=math.ceil(ASCII/36)
            pos=ASCII % 36
            for col in range(colStart,colStart+windowRowSize):
                for row in range(rowStart,rowStart+windowColSize):
                        posCount+=1
                        if posCount == pos:
                            imgNpArray[col][row]+=loopNumber
            colStart+=windowColSize                
            if( colStart == imageColumn):
                rowStart+=windowRowSize
                colStart=0
        cv2.imwrite("Test.png",imgNpArray)    
            
    def embadeMark(self,imgNpArray):
        imageRow,imageColumn=imgNpArray.shape[0],imgNpArray.shape[1]
        coordX=(imageRow*2)//3
        coordY=(imageRow*2)//3
        imgNpArray = cv2.circle(imgNpArray, (coordX,coordY),8, (0,0,255),0)
        return imgNpArray
    
