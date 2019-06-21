import os
import skimage
import numpy as np
import glob
import imageio as io


folderA = '/home/diego/Desktop/OnlyGreen_Balanced/testA_balanced'
folderB = '/home/diego/Desktop/OnlyGreen_Balanced/testB_balanced'




for file in os.listdir(folderA):
    imA = np.asarray(io.imread(folderA + '/' + file))
    imB = np.asarray(io.imread(folderB + '/' + file))
    image = np.concatenate((imB, imA), axis=1)
    io.imwrite('/home/diego/Desktop/OnlyGreen_Balanced/test_balanced/' + file + '.png', image)
