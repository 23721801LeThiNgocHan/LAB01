# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:57:46 2024

@author: PC
"""

var=input("Nhập 1 chữ cái: ")

if len(var)==1 and var.islower():
    print("Chữ cái in hoa là: ",var.upper())
elif len(var)==1 and var.upper():
    print("Chữ cái thường là: ",var.lower())
else:
    print("Hãy nhập lại 1 chữ cái")