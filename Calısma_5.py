# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 21:00:26 2023

@author: Hacer
"""
"""
# while ile faktöriyel
#while içindeki koşul doğru olduğu sürece çalışır.

sayi = int(input("sayı gir:"))
sayac=1
faktöriyel=1
while sayac <= sayi:
    faktöriyel = faktöriyel * sayac
    sayac += 1
print("Girdiğiniz sayi %s,\nFaktöriyel sonucu: %s"%(sayi,faktöriyel))



# for ile asal sayı

sayı = int(input("kaça kadar asal sayılarrı yazdıracağınızı belirtin:"))
print(2)

for i in range(3,sayı,1):
    kontrol = False
    for j in range(2,i):
        if i % j == 0:
            kontrol=True
    if kontrol == False:
        print(i)
        
#belirtilen sayı değerine kadar çift sayıların toplamı

sayi = int(input("kaça kadar çift sayılar toplansın :")) 
toplam = 0
for i in range(sayi):
    if(i %2 == 0):
        print(i)
        toplam = toplam + i
        i += 1
print("Toplamları:",toplam)    
           
# Karakter dizisindeki karakterlerin ve sayıların hesaplanması

veri = "Hacer Kırışoğlu"
liste = list(veri)
print(liste)
harf_sayıcı = 0
rakam_sayıcı = 0

for i in liste:
    if str(i).isdecimal():
        rakam_sayıcı += 1
    else:
        harf_sayıcı +=1
        
print("Rakam sayısı %s\nHarf sayısı %s"%(rakam_sayıcı,harf_sayıcı))

#for ile faktöriyel hesabı

sayi = int(input("faktöriyelini öğrenmek istediğin sayı:"))
faktöriyel = 1

for i in range(1,sayi + 1):
    faktöriyel *= i
    i += 1     
print("%s!: %s"%(sayi,faktöriyel))

# girilen sayıya kadar olan sayıların toplamını bulan

sayi = int(input("hangi sayıya kadar olan sayıların toplamını istiyorsunuz?"))
toplam = 0
for i in range(sayi):
    toplam = toplam + i
print("Sayıların toplamı ",toplam)    
"""
# for ile üs alma işlemi

us = int(input("üs:"))
sayı = int(input("sayı girin:"))
sonuc = 1

for i in range(1,(us + 1),1):
    sonuc *= sayı
print(sonuc)    


    


















    