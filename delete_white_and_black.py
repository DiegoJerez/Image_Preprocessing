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
            os.remove(file)
    print(n, 'white files removed')

def delete_black(folderA):
    os.chdir(folderA)
    n = 0
    for file in os.listdir(folderA):
        imA = io.imread(file)
        imA = imA == 0
        if imA.all():
            n = n + 1
            os.remove(file)
    print(n, 'black files removed')


delete_white('/home/default/Desktop/more_testing/pleasedelete/')
