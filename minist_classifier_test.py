# -*- coding: utf-8 -*-
"""
Created on Sat May 19 23:17:31 2018

@author: yong2
"""

import numpy as np
import struct
import matplotlib.pyplot as plt
import matplotlib.image as mpimg # mpimg 用于读取图片
import random
import pickle
from PIL import Image
from minstclass import Data
if __name__ == "__main__":
    with open("data", "rb") as file:       
        data = pickle.load(file)
        
        
        
#    #photo = mpimg.imread('0.bmp')
#    im = Image.open('0.bmp')
#    data.predict_online(photo)
    
    data.predict_online('5.bmp')