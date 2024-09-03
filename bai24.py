# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:53:07 2024

@author: PC
"""

a=int(input("Nhập giờ: "))
b=int(input("Nhập phút: "))
c=int(input("Nhập giây: "))

if 0<=a<24 and 0<=b<60 and 0<=c<60:
    print("Giờ,phút giây hợp lệ: ",f"{a}:{b}:{c}")
else:
    print("Không hợp lệ, hãy nhập lại")