import cv2,os
from sklearn.externals import joblib
import numpy as np
import csv

import glob
label = "1"
#run this script for all labels

f = open('csv/dataset.csv', 'a')
writer = csv.writer(f)
# header = ["label"]
# for i in range(784):
# 	header.append("pixel_"+str(i))

# writer.writerow(header)

a=0

dirList = glob.glob("orig_images/"+label+"/*.png")
for img_path in dirList:
	file_name = img_path.split("\\")[1]
	print(a,".",file_name)
	a = a+1
	im = cv2.imread(img_path)
	im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	im_gray = cv2.GaussianBlur(im_gray, (15, 15), 0)
	roi = cv2.resize(im_gray, (28, 28), interpolation=cv2.INTER_AREA)

	#cv2.imshow("window",roi)

	data=[]
	data.append(label)
	rows,cols = roi.shape

	

	# #Add pixel one-by-one into data Array.
	for i in range(rows):
	    for j in range(cols):
	        k = roi[i,j]
	        data.append(k)     

	writer.writerow(data)
	# cv2.imwrite("proc_images/0/"+file_name, roi)

	

