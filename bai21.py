# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:30:40 2024

@author: PC
"""

a=int(input("Nhập số = "))
b=["Không","Một","Hai","Ba","Bốn","Năm","Sáu","Bảy","Tám","Chín"]
if 0<=a<=9:
    print("Chữ tương ứng là: ",b[a])
else:
    print("Không đọc được")