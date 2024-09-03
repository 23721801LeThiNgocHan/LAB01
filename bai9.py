# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:51:09 2024

@author: PC
"""

print("**********MENU**********")
print("1.Hủ tiếu")
print("2.Cháo lòng")
print("3.Bánh canh")
print("4.Bún riêu")
print("5.Phở bò")
print("************************")

a=int(input("Mời nhập lựa chọn: "))
if a==1:
    print("Bạn chọn Hủ tiếu")
elif a==2:
    print("Bạn chọn Cháo lòng")
elif a==3:
    print("Bạn chọn Bánh canh")
elif a==4:
    print("Bạn chọn Bún riêu")
elif a==5:
    print("Bạn chọn Phở bò")
else:
    print("Không có trong thực đơn")