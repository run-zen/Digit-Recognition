import pyscreenshot as ImageGrab
import time
def capture() :
  images_folder = "F:/code heroku/digit recog new/digit recog/PCA/"
  im = ImageGrab.grab(bbox=(10, 150, 218, 358)) # X1,Y1,X2,Y2
  im.save(images_folder+str(0)+'.png')

	
