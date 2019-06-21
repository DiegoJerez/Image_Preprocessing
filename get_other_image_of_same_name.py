import os
import skimage
import numpy as np
import glob
import imageio as io
import numpy as np
import PIL
from PIL import Image
import shutil

files = os.listdir('/home/diego/Desktop/OnlyGreen_Balanced/trainA_balanced')
list = []
for file in files:
    split_name = file.split('.')
    list.append(split_name[0])
list.sort(key = float)
master = []
for file in list:
    name = file + '.png'
    master.append(name)

dir = '/home/diego/Desktop/OnlyGreen_Balanced/trainB'
newdir = '/home/diego/Desktop/OnlyGreen_Balanced/trainB_balanced'
for file in master:
    path = os.path.join(dir,file)
    newpath = os.path.join(newdir,file)
    shutil.move(path, newpath)
