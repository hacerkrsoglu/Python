# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 00:51:43 2023

@author: Hacer
"""
"""
# 1-100 arasında rastgale üretilecek bir sayıyı aşağı yukarı
ifadeleriyle buldurmaya çalışın.
** "random modülü" için "python random" şeklinde arama yapın
** 100 üzerinden puanlama yapın. Her soru 20 puan
**Hak bilgisini kullanıcıdan alın ve her soru belirtilen
can sayısı üzerinden hesaplansın.
random()
random modülünün random() adlı fonksiyonunu kullanarak,
0.0 ile 1.0 arasında rastgele bir kayan noktalı sayı üretebilirsiniz
uniform()belirli bir aralıkta kayan noktalı sayılar üretmek istediğimizde,
random() yerine uniform() adlı bir fonksiyon kullanacağız. 
randint()
kayan noktalı sayılar yerine tam sayılar üretmek de isteyebiliriz. 
İşte böyle bir durumda, random modülünün randint() adlı başka bir fonksiyonunu kullanabiliriz.
"""
"""
#1
import random
x = random.randint(1, 10)
can = int(input("Hak sayısını giriniz:"))
puan=100
while True:
    girdi = int(input("tahmininizi giriniz:"))
    if (girdi != x and girdi < x) :
        print("daha yüksek bir tahminde bulununuz")
        can -= 1
        puan -= 20
        if(can == 0):
            print("deneme hakkınız bitti")
            break
    elif (girdi != x and girdi > x ):
        print("girdiğiniz değerden daha küçük değer deneyin")
        can -= 1
        puan -= 20
        if(can == 0):
            print("deneme hakkınız bitti")
            break
    else:
        print("Doğru bildiniz. Tebrikler! Puanınız: %s"%(puan))
        break
       
print("Tahmin etmeniz gereken sayı %s"%(x))
"""

"""
#2
import random
sayi = random.randint(1,100)
can = int(input("Kaç hak kullanmak istersiniz:"))
hak = can 
sayac = 0
while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("tahmin: "))
    
    if sayi == tahmin:
        print("Tebrikler %s. defada bildiniz. Toplam puanınız: %s"%(sayac,(100 -(100/can)*(sayac - 1))))
        break
    elif sayi > tahmin :
        print("yukarı")
    else:
        print("aşağı")
    if hak == 0:
        print("Hakkınız bitti. Tutulan sayı %s"%(tahmin))
        
    
"""  