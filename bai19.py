# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:47:45 2024

@author: PC
"""

a=int(input("Nhập a= "))
b=int(input("Nhập b= "))
c=int(input("Nhập c= "))
d=int(input("Nhập d= "))

if a==b==c==d:
    print("Hãy nhập lại")
else:
   if a<=b and a<=c and a<=d:
      Sonhonhat = a
   elif b<=a and b<=c and b<=d:
      Sonhonhat = b
   elif c<=a and c<=b and c<=d:
      Sonhonhat = c
   else:
      Sonhonnhat = d
     
print("Số nhỏ nhất là: ",Sonhonhat)