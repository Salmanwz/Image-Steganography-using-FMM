#python library for computer vision
import cv2
class ImageRead:
    def __init__(self):
        pass
    
    #Method to read image in np array format
    def readImageNpArray(self,imgPath):
        img=cv2.imread(imgPath,0)#Reads image in grey scale mode
        return img
    
    #Method to display the image
    def showImage(self,imgPath):
        img=cv2.imread(imgPath)
        cv2.namedWindow('Test',cv2.WINDOW_AUTOSIZE)
        cv2.imshow('Test',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

