import os as os# helps navigate filesystem
from scipy.misc import imread, imresize, bytescale
from skimage import io #library for python to help access pictures
import numpy as np #help do math in python
import matplotlib.pyplot as plt
import random
import imageio
from PIL import Image

from skimage.util.shape import view_as_windows, view_as_blocks
from array import array
import argparse
import os
from math import log10
from os.path import join

import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
from torch.utils.data import DataLoader
import torch.backends.cudnn as cudnn

import torch
import torch.nn as nn
from torch.nn import init
import functools
from torch.optim import lr_scheduler
import argparse
import os
import torch
import torchvision.transforms as transforms



#curetesy of William Hahn
def load_data_make_jpeg(folder):

    img_size=(256,256, 3)
    img_new  = io.imread('/home/diego/MPFI/Images/CycleGAN_onlyGreen/Labels/onlygreen_labeled_1.png')
    img_new = img_new[:9984,:6912,:3]
    img_new_w = view_as_blocks(img_new, img_size)
    img_new_w = np.uint8(img_new_w)

    for i in range(img_new_w.shape[0]):
        for j in range(img_new_w.shape[1]):
#       #x = np.random.randint(img_new_w.shape[0])
#       #y = np.random.randint(img_new_w.shape[1])


            A = np.zeros((img_size[0], img_size[1], 3))
            A[:,:,:] = img_new_w[i,j,:,:]
            A = np.uint8(A)

            r = str(np.random.randint(99999999))

            imageio.imwrite('/home/whale/Desktop/combine/test/'+ r + '.jpg', A, quality = 100)




load_data_make_jpeg('/content/drive/My Drive/ID_Gold_Particles_2019/Data/')
