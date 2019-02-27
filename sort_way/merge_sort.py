# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 23:09:09 2019

@author: yong2

归并排序,先排好左边，右边，再通过一个辅助数组外排
"""

import numpy as np

def merge(list1,L,mid,R):
    """
    辅助数组进行外排，左边和右边混合在一起
    """
    help_list=[0]*(R-L+1)
    i,p1,p2=0,L,mid+1 #3个指针，哪个小就放入辅助数组
    #and布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
    # & 按位与运算符
    while p1 <= mid and p2 <= R :
        if list1[p1]<list1[p2]:
            help_list[i]=list1[p1] 
            p1+=1 
            i+=1
        else:
            help_list[i]=list1[p2]
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
    for i in range(0,len(help_list)):#将辅助数组赋值给list
        list1[L+i]=help_list[i]
    
def sortProcess(list1,L,R):
    """
    递归，宏观理解，先排左边再右边 O(N*logN)
    """
    if (L==R) :
        
        return 
#    mid=int((L+R)/2)
    mid=int(L+((R-L)>>1))
    sortProcess(list1,L,mid)#T(n/2)   
    sortProcess(list1,mid+1,R)#T(n/2)
    merge(list1,L,mid,R)#O(N)
    
def mergeSort(list1):
    if (len(list1)<2) :
        return
    sortProcess(list1,0,len(list1)-1)
    print(list1)
            
#list1=[2,7,5,4,1,5,6,8,3,10]
random_list=np.random.randint(10,size=4)
list1=list(random_list)  
#list1=[5,2,3,6,0,1,8,2,10]
sortProcess(list1,0,len(list1)-1)
#mergeSort(list1)