# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 00:09:59 2023

@author: Hacer
"""
"""
#Girilen sayının asal sayı olup olmadığını bulun
**Asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir
"""

sayi = int(input("Bir sayı giriniz:"))
asal_mi = True
if sayi == 1:
    asal_mi = False
    
 
for i in range(2,sayi):
    if (sayi % i == 0):
        asal_mi = False
        break
if asal_mi:
    print("%s asal bir sayıdır"%(sayi))
else:
    print("%s asal sayı değildir"%(sayi))
        










