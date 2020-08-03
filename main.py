import sys
from ImageRead import *
from ImageEncrypting import *
from ImageDecrypting import *
from Send import *
from recive import *

#Create objects for encrypting ,reading and decrypting
ImgRead=ImageRead()
ImageEncrypt=ImageEncrypting()
ImageSend=Send('127.0.0.1',50000)
#Get input and output paths
imgPath=sys.argv[1]
#Encrypt the message to array
img=ImgRead.readImageNpArray(imgPath)
ImageEncrypt.makeModuleFiveImage(img)
imgMarked=ImageEncrypt.embadeMark(img)
ImageEncrypt.encryptMessage(imgMarked,sys.argv[2])
ImgRead.showImage("Test.png")
print("Transmitting data....")
ImageSend.sendFile(imgPath)
ImageSend.sendFile(imgPath)
ImageSend.sendFile(imgPath)
ImageSend.sendFile(imgPath)
ImageSend.sendFile('Test.png')
