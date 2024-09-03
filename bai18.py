# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:54:28 2024

@author: PC
"""

a=input("Nhập giờ,phút,giây thứ nhất (VD.1h8p8s): ")
b=input("Nhập giờ,phút,giây thứ hai (VD.1h8p8s): ")

gio1=int(a.split("h")[0])
phut1=int(a.split("h")[1].split("p")[0])
giay1=int(a.split("p")[1].split("s")[0])

gio2=int(b.split("h")[0])
phut2=int(b.split("h")[1].split("p")[0])
giay2=int(b.split("p")[1].split("s")[0])
t1= gio1*3600 + phut1*60 + giay1
t2= gio2*3600 + phut2*60 + giay2
if 0<=gio1<24 and 0<=phut1<60 and 0<=giay1<60 and 0<=gio2<24 and 0<=phut2<60 and 0<=giay2<60:
  t=t1+t2
  g1=t//3600
  l1=(t/3600)-g1
  p1=(l1*60)//1
  i1=(l1*60)-p1
  s1= (i1*60)//1
  print(f"Tổng 2 giờ là:{g1} giờ {p1} phút {s1} giây")
else:
    print("Hãy nhập lại")

if t1<=t2:
   tt=t2-t1
   g2= tt//3600
   l2=(tt/3600)- g2
   p2=(l2*60)//1
   i2= (l2*60) - p2
   s2= (i2*60)//1
   print(f"Hiệu 2 giờ là:{g2} giờ {p2} phút {s2} giây")
elif t1>=t2:
     d=t1-t2
     g3=d//3600
     l3=(d/3600)-g3
     p3=(l3*60)//1
     i3=(l3*60)- p3
     s3= (i3*60)//1
     print(f"Hiệu 2 giờ là: {g3} giờ {p3} phút {s3} giây")
else:
 print("Không tính được kết quả")

