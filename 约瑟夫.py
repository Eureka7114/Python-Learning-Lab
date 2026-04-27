# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:46:19 2026

@author: 24159
"""

#定义约瑟夫函数完成出圈列表
def jos_func(n,m):
    """
     参数n,m : int n代表总人数,m代表出圈间隔序号数
     返回值：list:出圈列表  
    """
    result=[] #出圈列表
    #########begin############## 
    lb = [x for x in range(1,n+1)]
    idx = 0
    while lb:
        idx = (idx+m-1)%len(lb)
        result.append(lb.pop(idx))
    
    
    #########ends##############       
    return (result)
###############################
#主程序
n,m=eval(input())
jos_lst = jos_func(n,m)
print("出圈列表:")
print(jos_lst)