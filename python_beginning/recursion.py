# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:30:29 2019

@author: yong2
"""
'1、当函数直接返回时有基本实例'
'2、递归实例，包括一封或者多个问题较小部分的递归调用'
import numpy as np

def factorial(n):
    """n的阶乘"""
    if n==1:
        return 1
    else:
        return n*factorial(n-1)  
    
def power(x,n):
    """一个数x的幂"""
    if n==0:
        return 1
    else:
        return x*power(x, n-1)    
    
def binary_search(list2, des):
    """
    二分查找，查找列表中数字在第几位O(logN)
    """
    left=0
    right=len(list2)-1
    while (left <= right) :
        middle=int((left +right)/2)
        if list2[middle] == des :
            return middle
        elif list2[middle] < des:
            left=middle+1
        else:
            right=middle-1
    return ('没有该数字') 

def search(sequence, number, L, R):
    """递归实现二分查找"""
    if L==R:
#        print(sequence[L])    
        try: 
            assert number == sequence[R] #没有该数字时报错
        except: 
            print('没有该数字')
      
        return R
    else :
        middle = (L+R) // 2    
        if number > sequence[middle]:  #>对应middle+1,含=时对应middle
            return search(sequence, number, middle+1, R)
        else:
            return search(sequence,number, L, middle)
    
   
random_num=np.random.randint(10,size=10)
lista=sorted(random_num)
print(search(lista,5,0,9))
#print(power(2,2))    