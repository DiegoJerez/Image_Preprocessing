import os
import random
import shutil

dirA = '/home/diego/Desktop/OnlyGreen_Balanced/trainA_balanced'
newdirA = '/home/diego/Desktop/OnlyGreen_Balanced/testA_balanced'
dirB = '/home/diego/Desktop/OnlyGreen_Balanced/trainB_balanced'
newdirB = '/home/diego/Desktop/OnlyGreen_Balanced/testB_balanced'
for i in range (30):
    filename = random.choice(os.listdir(dirA))
    pathA = os.path.join(dirA,filename)
    pathB = os.path.join(dirB,filename)
    newpathB = os.path.join(newdirB, filename)
    newpathA = os.path.join(newdirA, filename)
    shutil.move(pathA, newpathA)
    shutil.move(pathB, newpathB)
