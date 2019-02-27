# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:28:14 2019

@author: yong2
"""
import numpy as np 

def fibonacci(num):
    '打印前num个数'
    fibs=[0,1]
#    num=input('How many Fibonacci numbers do you want? ')
    for i in range(int(num)-2):
        fibs.append(fibs[-2]+fibs[-1])
    print(fibs)

def fib(n):
    '返回数组中第n+1个数值，但该数下标为n'
    if n==0:
        result=0
    elif n==1:
        result=1
    else:
        result=fib(n-1)+fib(n-2)
    return result

random_num=np.random.randint(10)
print(fib(random_num))
fibonacci(random_num)