#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy


# In[2]:


from scipy.io import loadmat


# In[3]:


from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC


# In[4]:


X = np.array(loadmat('digit_dataSet.mat')['X'])
y = np.array(loadmat('digit_dataSet.mat')['y'])


# In[5]:


X.shape


# In[6]:


y.shape


# In[7]:


X[np.random.randint(X.shape[0], size=10), :]


# In[8]:


y[np.random.randint(y.shape[0], size=10), :]


# In[9]:


data = np.concatenate((X,y), axis=1)


# In[10]:


data.shape


# In[11]:


data = data[np.random.randint(data.shape[0], size=5000), :]


# In[12]:


x_train = data[0:3000,0:400]


# In[13]:


y_train = data[0:3000,400:401]


# In[14]:


x_train.shape


# In[15]:


y_train.shape


# In[16]:


x_test = data[3000:5001,0:400]


# In[17]:


y_test = data[3000:5001,400:401]


# In[18]:


x_test.shape


# In[19]:


y_test.shape


# In[20]:


clf = OneVsRestClassifier(SVC()).fit(x_test, y_test)

# get image
import cv2
path = r"F:\code heroku\digit recog new\digit recog\PCA\1.png"
img = cv2.imread(path,0)
imgnew  = img.reshape(1,400)
imgnew = imgnew - 40
img = imgnew.reshape(20,20)
cv2.imshow("image", img)
print(clf.predict(imgnew[0:1,:]))




