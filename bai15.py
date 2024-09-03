# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 04:01:04 2024

@author: PC
"""


a=float(input("Nhập a = "))
b=float(input("Nhập b = "))
x1= a+b
x2= (a**(1/3)) + (b**(1/3))
x3= (a*b)**(1/3)
x4= a**(1/3)
x5= b**(1/3)
T= ((x1/x2)-x3) / (x4 - x5)**2
print("Kết quả là: ",round(T,3))
