#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 09:45:40 2018

@author: li
"""

from keras.models import load_model
from addition_rnn import CharacterTable
import numpy as np
REVERSE = True
MAXLEN = 7


if __name__ == "__main__":
    model = load_model('rnn_add.h5')
    chars = '0123456789+ '
    ctable = CharacterTable(chars)
    while 1:
        input_data = input("please input your question:")
        
        input_data = input_data + ' ' * (MAXLEN - len(input_data))
        q = input_data
        input_data = input_data[::-1]
        input_data_vecter = ctable.encode(input_data, 7)
        input_data_vecter = input_data_vecter.astype(np.bool)
        input_data_vecter = input_data_vecter[np.newaxis,:]
        preds = model.predict_classes(input_data_vecter, verbose=0)
        guess = ctable.decode(preds[0], calc_argmax=False)
        print('answer:', guess)
            