# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:10:04 2024

@author: PC
"""

var=input("Nhập 1 chữ cái thường: ")

if len(var)==1 and var.islower():
    print("Chữ in hoa là: ",var.upper())
else:
    print("Nhập lại 1 chữ cái thường")

