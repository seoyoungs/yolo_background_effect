import albumentations as A
from albumentations.pytorch import ToTensorV2
import cv2
import os
import numpy as np
from PIL import Image
import re

file_list=os.listdir('C:/dacon/230220/123_image/3_output_txt')
file_list.sort()
file_na = 'C:/dacon/230220/123_image/3_output_txt/'
label_save = 'C:/dacon/230220/123_image/3_output_txt_flip/'


a,b,getnum=next(os.walk('C:/dacon/230220/123_image/3_output_txt_flip'))
count = len(getnum)




for i in file_list:
    path=file_na+i
    fr = open(path, 'r')
    lines = fr.readlines()
    lines_len = len(lines)

    z=0
    for j in lines:
        save_flip_txt= label_save + i
        File = open(save_flip_txt, "w")

        if z == lines_len:
            z = 0
        while z < lines_len:
            # print(lines_len)
            lines_1 = lines[z]
            lines_2 =  re.sub('1.000', '1', lines_1)
            File.write(lines_2)
            z +=1

        File.close()

        



