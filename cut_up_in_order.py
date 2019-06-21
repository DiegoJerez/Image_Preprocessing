import os as os# helps navigate filesystem
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

Image.MAX_IMAGE_PIXELS = None

#curetesy of William Hahn
def load_data_make_jpeg():

    img_size=(256,256, 3)
    img_new  = io.imread('/home/diego/MPFI/Images/041719 JCFFRIL 07 Wt3 profile 13 Spiny top montage color for Diego.tif')
    #img_ref  = io.imread('/home/diego/MPFI/Images/CycleGAN_onlyGreen/Unlabels/onlygreen_2.png')
    img_new = img_new[:9984,:16128,:3]
    #img_ref = img_ref[:7424,:5632,:3]

    img_new_w = view_as_blocks(img_new, img_size)
    img_new_w = np.uint8(img_new_w)
    #img_ref_w = view_as_blocks(img_ref, img_size)
    #img_ref_w = np.uint8(img_ref_w)
    r = 0
    for i in range(img_new_w.shape[0]):
        for j in range(img_new_w.shape[1]):

            A = np.zeros((img_size[0], img_size[1], 3))
            #B = np.zeros((img_size[0], img_size[1], 3))

            A[:,:,:] = img_new_w[i,j,:,:]
            #B[:,:,:] = img_ref_w[i,j,:,:]
            A = np.uint8(A)
            #B = np.uint8(B)
            imageio.imwrite('/home/diego/MPFI/Datasets/profile13_numbered/'+ str(r) + '.png', A)
            #imageio.imwrite('/home/diego/MPFI/Datasets/OnlyGreen/trainB/'+ str(r) + '.png', B)
            r += 1



load_data_make_jpeg()
