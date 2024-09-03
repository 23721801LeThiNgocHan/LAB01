# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:18:08 2024

@author: PC
"""

print ("1:vuông")
print("2:chữ nhật")
print("3:tròn")
a=int(input("Nhập hình: "))

if a==1:
    c=float(input("Cạnh = "))
    print("P= ",c*4)
    print("S= ",c*c)
elif a==2:
    b=float(input("Chiều rộng = "))
    d=float(input("Chiều dài = "))
    print("P= ",(b+d)*2)
    print("S= ",b*d)
elif a==3:
    r=float(input("Bán kính = "))
    print("P= ",r*2*3.14)
    print("S= ",r*r*3.14)
else:
    print("Xin hãy nhập lại")