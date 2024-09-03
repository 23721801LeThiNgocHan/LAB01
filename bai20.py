# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:22:36 2024

@author: PC
"""

a=int(input("Nhập a= "))
b=int(input("Nhập b= "))
c=int(input("Nhập c= "))

if a==b==c:
    print("Hãy nhập lại")
else:
    if a>=b and a>=c:
        lonnhat = a
    if b>=a and b>=c:
        lonnhat = b
    else:
        lonhat = c
print("Số lớn nhất là: ",lonnhat)