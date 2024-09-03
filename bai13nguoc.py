# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 03:44:26 2024

@author: PC
"""

a=input("Nhập ngày/tháng/năm: ")
ngay,thang,nam = a.split("/")
print(f"Ngày {ngay},Tháng {thang},Năm {nam}")
print(f"Ngày {ngay},Tháng {thang},Năm {str(nam) [2:]}")
print(f"Năm {nam},Tháng {thang},Ngày {ngay}")

    
