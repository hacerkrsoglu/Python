# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:30:48 2023

@author: Hacer
"""

"""
Döngüler
***********************************************
For Döngüsü
numbers = [1,2,3,4,5]
for değişken_ismi in numbers:
    print(değişken_ismi)

listenin içerisinden tek tek elemanları al ve bunları değişken_ismi nin içine at
her döngüde içindekini yazdır.b  
dictionary de tam olarak böyle olmuyor.

d = {"k1":1, "k2":2, "k3":3}

for item in d.items():
    print(item)
for key,value in d.items():
    print(key,value)

-Uygulamalar-
sayilar = [1,3,5,7,9,12,19,21]
#sayılar listesindeki hangi sayılar 3 ün katıdır?

for i in sayilar:
    if (i %3 == 0):
        print(i)


#sayılar listesinde sayıların toplamı kaçtır?
sayilar = [1,3,5,7,9,12,19,21]
toplam = 0
for i in sayilar:
    toplam +=  i
    print("toplam:",toplam)
    
#listedeki tek sayıların karesini alın
sayilar = [1,3,5,7,9,12,19,21]
for i in sayilar:
    if (i %2 != 0): # veya sayi %2 == 1 
        print(i**2)

# şehirlerden hangileri en fazla 5 karakterldir?
sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]
for sehir in sehirler:
    if(len(sehir) <= 5 ):
        print(sehir)
#ürünlerin fiyatları toplamı nedir ? 
urunler = [
    {"name":"samsung S6","price": "3000"},
    {"name":"samsung S7","price": "4000"},
    {"name":"samsung S8","price": "5000"},
    {"name":"samsung S9","price": "6000"},
    {"name":"samsung S10","price": "7000"}
    ]
toplam = 0
for urun in urunler:
    fiyat = int(urun["price"])
    toplam += fiyat
    print("toplam:",toplam)
    
#ürünlerden fiyatı en fazla 5000 olan ürünleri gösterin

urunler = [
    {"name":"samsung S6","price": "3000"},
    {"name":"samsung S7","price": "4000"},
    {"name":"samsung S8","price": "5000"},
    {"name":"samsung S9","price": "6000"},
    {"name":"samsung S10","price": "7000"}
    ]

for urun in urunler:
    fiyat = int(urun["price"])
    if(fiyat <= 5000):
        print(urun["name"],fiyat)       

*****************************************************
-While  Döngüsü        
"""






















