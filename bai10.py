# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:57:56 2024

@author: PC
"""

a=int(input("Nhập số xe: "))
nghin = a//1000
s=a%1000
tram =s//100
r=s%100
chuc = r//10
don_vi = r%10
T=nghin+tram+chuc+don_vi
if 1000<=a<9999:
    print("Số xe của bạn được",T,"nút")
else:
    print("Nhập lại số xe với 4 chữ số")