# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 03:17:32 2024

@author: PC
"""

a=int(input("Nhập ngày: "))
b=int(input("Nhập tháng: "))
c=int(input("Nhập năm: "))
#câu a
if 1<=a<31 and 1<=b<12 and 0<c:
    print("Ngày tháng năm sinh là: ",f"{a}/{b}/{c}")
    print("Ngày tháng năm sinh là: ",f"{a}/{b}/{str(c) [2:]}")
    print("Ngày tháng năm sinh là: ",f"{c}/{b}/{a}")
else: 
    print("Không định dạng được")


