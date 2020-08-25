# This is the start of code

# reading data i.e image for dimensionnality reduction
def get_image() :
    
  import screencapture
  import cv2
  folder = r"F:\code heroku\digit recog new\digit recog\PCA"
  screencapture.capture()
  path = folder + "\\"+ str(0) + ".png"
  img = cv2.imread(path, 0 )                         # the image is in 'img'
  dim = (20,20)
  resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
  return resized



