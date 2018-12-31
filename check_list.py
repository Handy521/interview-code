# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:09:21 2018

@author: yong2
"""
#找出两个有序list中重复元素
import numpy
import datetime
def fun_x(x):
    x = x + 1
    return x
def fun_y(y):
    y = y + 1
    return y
def check_list(L1, L2, L3, x=0, y=0):
    while x < len(L1) and y < len(L2):
        if L1[x] > L2[y]:
            y = fun_y(y)
        elif L1[x] < L2[y]:
            x = fun_x(x)
        elif L1[x] == L2[y]:
            L3.append(L1[x])
            x = fun_x(x)
            y = fun_y(y)
        else:
            pass
    return L3
a = numpy.random.randint( 5,100000,100000 )
b = numpy.random.randint( 5,100000,100000 )
#set1 = set(list1)#如果每一个列表中均没有重复的元素
#set2 = set(list2)
#print (set1 & set2)
list1 = sorted(list(a))
list2 = sorted(list(b))
startt1 = datetime.datetime.now()
print(fund_loacation(list1, list2, []))
endt1 = datetime.datetime.now()
print(endt1 - startt1)
