# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:42:02 2024

@author: PC
"""

a=float(input("Nhập cân nặng (kg): "))
b=int(input("Nhập chiều cao (cm): "))
c=b/100
S=a/(c**2)
print("BMI của bạn là: ",round(S,3))