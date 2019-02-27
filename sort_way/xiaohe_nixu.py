# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:30:22 2019

@author: yong2
"""

import numpy as np

def small_sum(arr):
    """
    一个数组中，每一个数左边比当前数小的数累加起来，叫做该数组的小和 O(N^2)
    """
    small_sum=[]
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[j]<arr[i]:
                small_sum.append(arr[j])
    
    return small_sum

def reverse_sort(arr):
    """
    打印逆序对，一个数组中左边的数比右边大，打印这两个数
    """
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[j]>arr[i]:
                print(arr[j],arr[i])

def merge(list1,L,mid,R):
    """
    辅助数组进行外排，左边和右边混合在一起 O(N*logN)
    """
    help_list=[0]*(R-L+1)
    i,p1,p2=0,L,mid+1
    res=0
    #and布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
    # & 按位与运算符
    while p1 <= mid and p2 <= R :
        if list1[p1]<list1[p2]:
            res += (R-p2+1)*list1[p1] #有多少个数大于当前数，一批一批包含            
            help_list[i]=list1[p1]          
            p1+=1 
            i+=1        
        else:
            help_list[i]=list1[p2]
            print(list1[p1],list1[p2]) #打印逆序对 (if 改成<=)
            for j in range(p1+1,mid+1):
                print(list1[j],list1[p2])#P1后的数都大于当前P2所指的数a
            p2+=1
            i+=1    
    #两个必有一个越界，把没越界的数拷贝到help    
    while (p1<=mid):
        help_list[i]=list1[p1]
        i+=1
        p1+=1
    while (p2<=R):
        help_list[i]=list1[p2]
        i+=1
        p2+=1
    for i in range(0,len(help_list)):
        list1[L+i]=help_list[i]
#    print(res)#多次累加和
    return res

def mergeSort(arr,L,R) :
    if (L==R):
        return 0
    mid=int(L+((R-L)>>1))
    #左侧小和加右侧小和加合并产生的小和
    return mergeSort(arr,L,mid)+mergeSort(arr,mid+1,R) + merge(arr,L,mid,R)
                        
random_list=np.random.randint(10,size=10)
list1=list(random_list)  
#list1=[1,4,3,2,5,1]
b=small_sum(list1)
#c=reverse_sort(list1)
a=mergeSort(list1,0,9)
print(sum(b))