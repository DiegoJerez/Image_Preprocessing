import os
import skimage
import numpy as np
import glob
import imageio as io
import numpy as np

def combine_white(folderA):
    os.chdir(folderA)
    for file in os.listdir(folderA):
        imA = io.imread(file)
        newimage = np.concatenate((imA,white), axis=1)
        r = str(np.random.randint(99999999))
        io.imwrite('/home/diego/MPFI/Datasets/profile13_numbered_combined/' + file + '.png', newimage)

white = io.imread('/home/diego/MPFI/Datasets/white_images/white.png')

combine_white('/home/diego/MPFI/Datasets/profile13_numbered')
