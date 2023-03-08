# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 19:09:57 2023

@author: kavin
"""



import os
import cv2
from PIL import Image
import numpy as np
# 

# 
data=[]
labels=[]
# 
# ----------------
# LABELS
# aphids 0
# worm 1
# bact 2
# power 3
# targedted 4
# healthy 5
# ----------------

# Cat 0 "E:\BACKUPS\BACKUPS\projects\CNN\PLANT_DISEASE\Aphids edited"
Aphids = os.listdir(os.getcwd() + "/PLANT_DISEASE/Aphids edited/")
for x in Aphids:
    imag=cv2.imread(os.getcwd() + "/PLANT_DISEASE/Aphids edited/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(0)

#Dog 1 "E:\BACKUPS\BACKUPS\projects\CNN\PLANT_DISEASE\Army worm edited"
worm = os.listdir(os.getcwd() + "/PLANT_DISEASE/Army worm edited/")
for x in worm:
    imag=cv2.imread(os.getcwd() + "/PLANT_DISEASE/Army worm edited/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(1)

# lion 2"E:\BACKUPS\BACKUPS\projects\CNN\PLANT_DISEASE\Bacterial Blight edited"
bact = os.listdir(os.getcwd() + "/PLANT_DISEASE/Bacterial Blight edited/")
for x in bact:
    imag=cv2.imread(os.getcwd() + "/PLANT_DISEASE/Bacterial Blight edited/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(2)

# tiger 3 "E:\BACKUPS\BACKUPS\projects\CNN\PLANT_DISEASE\Powdery Mildew Edited"
power = os.listdir(os.getcwd() + "/PLANT_DISEASE/Powdery Mildew Edited/")
for x in power:
    imag=cv2.imread(os.getcwd() + "/PLANT_DISEASE/Powdery Mildew Edited/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(3)

# kurama 4 "E:\BACKUPS\BACKUPS\projects\CNN\PLANT_DISEASE\Target spot edited"
targeted = os.listdir(os.getcwd() + "/PLANT_DISEASE/Target spot edited/")
for x in targeted:
    imag=cv2.imread(os.getcwd() + "/PLANT_DISEASE/Target spot edited/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(4)
    
# kurama 4 "E:\BACKUPS\BACKUPS\projects\CNN\PLANT_DISEASE\Healthy leaf edited"
health = os.listdir(os.getcwd() + "/PLANT_DISEASE\Healthy leaf edited/")
for x in health:
    imag=cv2.imread(os.getcwd() + "/PLANT_DISEASE\Healthy leaf edited/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(4)




disease=np.array(data)
labels=np.array(labels)
# 
np.save("disease",disease)
np.save("labels",labels)