# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 01:30:59 2023

@author: Hacer
"""
"""
a= int(input("x^2li terimin katsayısı:"))
b= int(input("xli terimin katsayısı:"))
c= int(input("sabit terimin katsayısı:"))
denklem =(" (a)*(x**2) + (b)*x + c")

delta=b**2-4*a*c


if(delta >= 0):
    x1=(-b-delta**0.5)/(2*a)
    x2=(-b+delta**0.5)/(2*a)
    print("Birinci Kök : {}\nİkinci Kök : {}".format(x1,x2))
else:
    print ("denklemin reel kökü yok.")
    
"""


"""
karakter_dizisi = input("Bir kelime giriniz:")

if karakter_dizisi.isdigit():
    print("Lütfen karakter dizisi giriniz.")    
else:
    print("Girdiğiniz kelimenin tersi : {0}".format(karakter_dizisi[::-1]))
"""

sayı = int(input("Pozitif sayı giriniz:"))

toplam = 0
for i in range(sayı):
    islem = sayı / 2.0
    if (islem == 0.1) or (islem < 0.1):
        print(toplam)
        break
    toplam = toplam + islem
    
    sayı = islem

print("Sonuç: ", toplam)











"""
sayı = int(input("Pozitif sayı giriniz:"))
toplam = 0.0
while :
    islem = sayı / 2.0
    
    if (islem == 0.1) or (islem < 0.1):
        print(toplam)
        break
    toplam = toplam + islem
    
    sayı = islem

print("Sonuç: ", toplam)

"""
























