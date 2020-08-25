import pyscreenshot as ImageGrab
import time

images_folder = "orig_images/1/"

for i in range (0,100) :
  time.sleep(1)
  if (i % 3 == 0):
    time.sleep(6)
  im = ImageGrab.grab(bbox=(10, 160, 218, 368)) # X1,Y1,X2,Y2
  print ("saved....",i)
  im.save(images_folder+str(i)+'.png')
  print ("clear screen now and redraw now...")
	
