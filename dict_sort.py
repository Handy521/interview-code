# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:55:47 2018

@author: yong2
"""

def dictSort(n, k):
    n=int(n)
    k=int(k)
    num_list = []
    
    for i in range(n):
        num_list.append(i + 1)
    
    list = []
    a = n // 10
    
    for j in range(9):
        if j <= a:
            list.append(num_list[j])
            for m in range(j*10 + 9, j*10+19):
                if m < len(num_list):
                    list.append(num_list[m])
        else:
            list.append(num_list[j])
    print(list)
    return list[k-1]
n, k = input("Please input the num n and the k：").split()

print(dictSort(n,k))
