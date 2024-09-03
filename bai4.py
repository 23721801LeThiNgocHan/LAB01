# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:18:06 2024

@author: PC
"""

N=int(input("Nhập số nguyên dương N = "))
S=(N//10)+(N%10)
if 10<=N<=99:
    print("Chữ số thứ nhất: ",N//10)
    print("Chữ số thứ hai: ",N%10)
    print("Tổng 2 số là: ",S)
else:
    print("xin hãy nhập lại số nguyên dương N có 2 chữ số")