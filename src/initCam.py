from picamera import PiCamera 
from datetime import datetime
from PIL import Image
import os

class imgControler:
    def __init__(self, res = (900,900), outFolder = "./output/"):
        self.res = res
        devName = os.uname()[1]
        currTime = datetime.now().strftime("%m-%d-%y_%H:%M:%S")
        fname = "{}_{}.jpg".format(devName, currTime )
        self.fpath = os.path.join(outFolder, fname)
     
    def getImg(self):
        cam = PiCamera()
        cam.resolution = self.res
        cam.capture(self.fpath)
        
    def cropImg(self):
        img = Image.open(self.fpath)
        width, height = img.size
        left=280
        top=450
        right =550
        bottom = 700
        imgOut=img.crop((left, top, right, bottom))
        imgOut.save(self.fpath)