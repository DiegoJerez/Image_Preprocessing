import os
import skimage
import numpy as np
import glob
import imageio as io
import numpy as np


A = np.zeros((256,256,3))
A = np.uint8(A)
io.imwrite('/home/diego/MPFI/Datasets/white_images/white.png', A)
#for file in os.listdir('/home/whale/Desktop/combine/testA'):
#        io.imwrite('/home/whale/Desktop/combine/testB/' + file + '.jpg', A, quality = 100)
