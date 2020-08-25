import pyscreenshot as ImageGrab
import time

images_folder = "F:\code heroku\digit recog new\digit recog\orig_images\5"

for i in range (0,1000):
	
            time.sleep(7)
            im = ImageGrab.grab(bbox=(10, 150, 218, 358)) # X1,Y1,X2,Y2
            print ("saved....",i)
            im.save(images_folder+str(i)+'.png')
            print ("clear screen now and redraw now...")
            
