from ImageRead import *
import sys
import numpy
import math
class ImageDecrypting:
    def __init__(self):
        pass


    #Method to decrypt the message using the five-modulous method
    def decryptMessage(self,imgNpArray):
        windowRowSize=6
        windowColSize=6
        hiddenString=""
        imageRow,imageColumn=imgNpArray.shape[0],imgNpArray.shape[1]
        totalBlocks=(imageRow*imageColumn)//(windowRowSize*windowColSize)
        colStart=0
        rowStart=0
        for block in range(0,totalBlocks):
            Found=False
            posCount=-1
            for col in range(colStart,colStart+windowRowSize):
                for row in range(rowStart,rowStart+windowColSize):
                    posCount+=1
                    if imgNpArray[col][row]%5 != 0:
                        loopNumber=imgNpArray[col][row]%5-1                        
                        pos=posCount                        
                        ASCII=(36*(loopNumber))+pos                                                
                        hiddenString=hiddenString+(chr(ASCII))
                        Found=True                        
            if not Found:
                return hiddenString
            colStart+=windowColSize                
            if( colStart == imageColumn):
                rowStart+=windowRowSize
                colStart=0

