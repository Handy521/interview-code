# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:25:02 2019

@author: yong2
"""

'''
sort_way
'''
#import numpy as np

def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
    
def bubble_sort(list1):
    """
    冒泡排序,最大的沉底O(N^2)
    """
    n=len(list1)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if (list1[j]>list1[j+1]):#相邻的比较
                list1[j],list1[j+1]=swap(list1[j],list1[j+1])
    return list1

def binary_search(list2,des):
    """
    二分查找，查找列表中数字在第几位O(logN)
    """
    left=0
    right=len(list2)-1
    while ( left <= right ) :
        middle=int( (left +right )/2 )
        if list2[middle] == des :
            return middle
        elif list2[middle] < des:
            left=middle+1
        else:
            right=middle-1
    return ('没有该数字')
        
def search_sort(list1):
    """
    选择排序，每次选择最小的方前面O(N^2)
    """
    n=len(list1) 
    for i in range(n):
        for j in range(i+1,n):
            if (list1[i]>list1[j]):#第一个和之后的进行比较
                list1[i],list1[j]=swap(list1[i],list1[j])
    return list1 

def insert_sort(list1):
    """
    从第一个元素开始，j的范围就是前面位置，相邻比较O(N)~O(N^2)最差估计时间复杂度
    """
    n=len(list1)
    for i in range(n):
        for j in range((i-1),-1,-1):#倒序从后（-1能取到边界值）向前，步长-1，最后为0
            if (list1[j]>list1[j+1]):#相邻的比较
                list1[j],list1[j+1]=swap(list1[j],list1[j+1])
    return list1 

def get_max(list1,L,R):
    """
    递归，压栈保存当前所有信息到栈，子过程返回后，顺序执行
    """
    if (L==R) :
        return list1[L]
    mid=int((L+R)/2)
    maxleft=get_max(list1,L,mid)
    maxright=get_max(list1,mid+1,R)
    return max(maxleft,maxright)
    
        
    
list1=[2,7,5,4,1,5,6,8,3]
#mearge=code_01_Mergesort()          
#mearge.mergeSort(list1)        
#a=bubble_sort(list1)
#a=search_sort(list1)
#a=insert_sort(list1)
#print(a)
#b=binary_search(a,4)
#print(b)
a=get_max(list1,0,len(list1)-1)
#mergeSort(list1)