# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:46:07 2019

@author: yong2
"""

def hanno (n,x,y,z) :
    if n==1 :
        print(x,'-->',z)
    else:
        hanno(n-1,x,z,y)#将n-1个盘子从X移动到y
        print(x,'-->',z)#将最底下的盘子移动到Z
        hanno(n-1,y,x,z)#将y上的盘子移到z上
#    print('============')  
    return 0
#n=int(input('输入一个整数：'))
#hanno(1,'a','b','c')
#hanno(3,'a','b','c')
hanno(2,'x','y','z')
#hanno(4,'a','b','c')