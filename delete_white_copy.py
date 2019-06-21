import os
import skimage
import numpy as np
import glob
import imageio as io

def delete_white(folderA):
    os.chdir(folderA)
    n = 0
    for file in os.listdir(folderA):
        imA = io.imread(file)
        imA = imA == 255
        if imA.all():
            n = n + 1
            imB = io.imread('/home/diego/MPFI/Datasets/OnlyGreen/trainB/' + file)
            imB = imB == 255
            if imB.all():
                os.remove('/home/diego/MPFI/Datasets/OnlyGreen/trainB/' + file)
                os.remove(file)
            else:
                print(file)
    print(n, 'white files removed')



delete_white('/home/diego/MPFI/Datasets/OnlyGreen/trainA')
