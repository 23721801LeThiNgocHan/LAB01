# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:24:32 2024

@author: PC
"""

time=input("Nhập giờ phút giây dưới dạng ':' ")
hh, mm, ss = map(int, time.split(":"))
if 0<= hh <24 and 0<= mm <60 and 0<= ss <60:
    T= hh*3600 + mm*60 + ss
    print("Tổng số giây là: ",T)
else:
    print("Không định dạng được")