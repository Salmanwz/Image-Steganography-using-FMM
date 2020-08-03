import sys
from ImageDecrypting import *
from ImageRead import *

ImgDecrypt=ImageDecrypting()
outputPath=sys.argv[1]
ImgRead=ImageRead()
img=ImgRead.readImageNpArray(outputPath)
hiddenMessage=ImgDecrypt.decryptMessage(img)
print("The hidden message is ",hiddenMessage)