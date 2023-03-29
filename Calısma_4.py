# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:43:38 2023

@author: Hacer
"""
"""
Problem 1
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse
bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)


sayi = int(input("sayı giriniz:"))
i = 1
toplam = 0
while (i < sayi):
    
    if(sayi %i == 0):
        toplam = toplam + i
    i += 1   
if(toplam == sayi):
    print(sayi,"mükemmel bir sayıdır")
        
else:
    print(sayi," mükemmel bir sayı değildir")
         

Problem 2
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan
herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse
bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4    

sayı = input("Sayı:")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while (gecici_sayı > 0):
    
    basamak = gecici_sayı % 10
    
    toplam += basamak ** basamak_sayisi
    
    gecici_sayı //= 10
    

if (toplam == sayı):
    print(sayı,"bir armstrong sayısıdır.")
else:
    print(sayı,"bir armstrong sayısı değildir.")


Problem 3
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

*İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları 
range() fonksiyonunu kullanarak elde edin.

for i in range(1,11):
    print("*********************************")
    for j in range(1,11):
        print("%s x %s = %s"%(i,j,(i*j)))

Problem 4
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği s
ayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı 
zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

*İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı
 q'ya basarsa döngüyü break ile sonlandırın.*
 
 
print("Bilgilendirma\nq ya bastığınızda döngüden çıkar")
toplam = 0
while True:
    n = input("sayı girin:")
    if(n == "q"):
        break   
    n = int(n)
    toplam += n
print("Girdiğiniz sayıların toplamı:",toplam)        



Problem 5
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın.
Bu işlemi *continue* ile yapmaya çalışın.

for i in range(1,101):
    if(not(i %3 == 0)):
        continue
    print(i) 
    
    
Problem 6
list comprehension kullanarak 1'den 100'e kadar olan sayılardan 
sadece çift sayıları bir listeye atmayı yapmayı çalışın.    


list = []

for i in range (1,101):
    if (i %2 == 0):
        list.append(i)
print(list)        


liste = [x for x in range(1,101) if x %2 == 0]
print(liste)

"""



















