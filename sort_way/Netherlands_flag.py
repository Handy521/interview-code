# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 10:59:22 2019

@author: yong2
"""

import numpy as np

def swap(a,b):
    temp=a
    a=b
    b=temp
    return(a,b)
    
def partition_simple(arr,L,R,num):
    """
    将一个数组中小于等于num的数放在数组的左边，大于num的数放在数组右边
    """
    x=L-1
    for i in range(R):
        if arr[i] <= num:
            arr[x+1],arr[i]= swap(arr[x+1],arr[i])
            x+=1
    print(arr)        
 
def Netherlands_flag(arr,L,R,num):
    """
    将一个数组中小于num的数放在数组的左边，等于num放中间，大于num的数放在数组右边
    """
    less=L-1
    more=R+1    
    while(L<more):
        if arr[L] <num:
            arr[less+1],arr[L]= swap(arr[less+1],arr[L])
            less+=1
            L+=1
        elif arr[L] >num:
            arr[more-1],arr[L]= swap(arr[more-1],arr[L])
            more-=1
        else:
            L+=1
    print(arr)  
    return [less+1,more-1]

def partition(arr,L,R):
    """
    将一个数组中小于num的数放在数组的左边，等于num放中间，大于num的数放在数组右边
    """
    less=L-1
    more=R    #数组最后一个数不参与遍历
#    num=arr[R] #取数组最后一个数划分
    while(L<more):
        if arr[L] <arr[R]:
            arr[less+1],arr[L]= swap(arr[less+1],arr[L])
            less+=1
            L+=1
        elif arr[L] >arr[R]:
            arr[more-1],arr[L]= swap(arr[more-1],arr[L])
            more-=1
        else:
            L+=1
    arr[more],arr[R]= swap(arr[more],arr[R]) #调整最后一个数的位置
    return [less+1,more]  #返回等于num两个边界值 

def quick_sort(arr,L,R):
    """
    快排O(N*logN)~O(N^2)
    """
    if(L<R):
        rand_num=np.random.randint(R-L+1)#随机快排，每次选一个随机位置数划分
        arr[L+rand_num],arr[R]=swap(arr[L+rand_num],arr[R])#O(N*logN)
        p=partition(arr,L,R)
        quick_sort(arr,L,p[0]-1)
        quick_sort(arr,p[1]+1,R)

random_list=np.random.randint(-20,100,size=10)
list1=list(random_list) 
#a=Netherlands_flag(list1,0,len(list1)-1,5)        
quick_sort(list1,0,len(list1)-1)   
print(list1)         
    