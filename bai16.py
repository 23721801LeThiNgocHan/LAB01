# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:41:03 2024

@author: PC
"""

a=input("Nhập giờ phút giây(VD.1h8p8s): ")
gio=int(a.split("h")[0])
phut=int(a.split("h")[1] .split("p")[0])
giay=int(a.split("p")[1].split("s")[0])
t=gio*3600 + phut*60 + giay
if 0<=gio<24 and 0<=phut<60 and 0<=giay<60:
    print("Số giây là: ",t)
else:
    print("Hãy nhập lại")