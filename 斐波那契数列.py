# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:19:13 2026

@author: 24159
"""

#判断一个数是否是素数
def isprime(x):
    """
     参数x : int
     返回值： True or False
    """
    #####begin######
    if x < 2:
        return True
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
    
    
    #####ends###### 
    
#求斐波那契数列的前n项保存在列表中
def fibnacci(n):
    """
     参数n : int 
     返回值： list :前n项斐波那契数列列表
    """
    #####begin######
    if n <= 0:
        return []
    if n == 1:
        return [1]
    list = [1,1]
    while len(list) < n:
        list.append(list[-1]+list[-2])
    return list
    
    
    #####ends######

#主程序
n = eval(input()) #输入斐波那契数列项数
#函数调用求解前n项斐波那契素数序列并输出
#####begin######
list1 = [x for x in list if isprime(x) == True]    
print(list1)
    
    
#####ends######