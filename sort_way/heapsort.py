# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 09:46:36 2019

@author: yong2
heap_sort
"""

import numpy as np

def swap(arr,a,b):
    """swap arr a and b"""
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp

def heapinsert(arr,index):
    """将数组转换成大根堆 """
    while (arr[index]>arr[int((index-1)/2)]):
        swap(arr,index,int((index-1)/2))
        index=int((index-1)/2)

def heapify(arr,index,size):
    """当大根堆一个数变化时，重新变成大根堆
    args index 从变化位置数父节点开始，和它的两个孩子比较
         size 需要的大根堆大小
    """
    left=index*2+1
    while (left < size):
        left=left+1 if (arr[left+1] >= arr[left] and left+1<size) else left
        if arr[left] > arr[index]:
            swap(arr, left, index)
        else:
            break
        index=left
        left=index*2+1
            
    

def heapsort(arr):
    """堆排序
    """
    if (arr==None or len(arr)<2):
        return
    for i in range(len(arr)):
        heapinsert(arr,i)        
    size=len(arr)-1
    '每次将最后一个数和堆顶交换，减少堆的大小，剩下的数再排成大根堆'
    '堆顶每次都为大根堆的最大值'
    swap(arr,0,size)
    while (size>0):
        heapify(arr,0,size)
        size-=1
        swap(arr,0,size)

random_list=np.random.randint(-20,100,size=10)
list1=list(random_list) 
#heapinsert(list1,len(list1)-1)
heapsort(list1)
