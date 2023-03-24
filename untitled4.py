# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:23:53 2023

@author: Hacer
"""

x,y,z = 2,4,5

numbers = 1,2,3,4,5

# kullanıcıdan aldığımız 2 sayının çarpımı ile x,y,z toplamının farkı

"""1.
sayi_1 = int(input("1.sayıyı gir:"))
sayi_2 = int(input("2sayıyı gir:"))
 
carpım = sayi_1 * sayi_2
toplam = x + y + z
fark = carpım - toplam
print("fark sonucu = " ,fark)
"""

# y nin xe kalansız bölümü // bununla yapılır
"""2.
a= y // x
print(a)
"""
# y nin x. kuvveti
"""3.
result = y**x
print(result)
"""
# x,*y,z = numbers işlemine göre znin küpü kçtır
# *y demek x y z normalde numberse direkt atanamaz 
#ama *y yaptığımızda ynin içine dizi olarak yerleştirir
#paylaştırcak şekilde 
"""4.
numbers = 1,2,3,4,5
x , *y ,z = numbers
result= z**3
print (result)
"""
#Girilen iki sayıdan hangisi büyüktür?
"""5.
a=int(input("1.sayı gir:"))
b=int(input("2.sayıyı gir:"))
result = a > b
print("{0} b:{1} den büyüktür".format(a,b),result)
"""

#kullanıcadan 2 vize(%60) ve final (%40) nnotunu alıp ortalama hesaplayınız
#ort 50nin üstündeyse geçti değilse kaldı

"""7.
vize1= float(input("1.vize not: "))
vize2=float(input("2.vize not:"))
final = float(input("final notu:"))

ort= ((((vize1 + vize2)/2)*0.6) + ((final)*0.4))
print("Ders ortalamanız {0} ve dersten geçme durumu {1}".format(ort,ort >=50))
 """   
#girlen sayı tek mi çift mi
"""8.
a=int(input("sayı gir:"))

b = (a%2 ==0)
print("çift olma durumu:",b)
"""
#parola ve email bilgisinin kontrolü
"""9.
email="hacer@gmail.com"
password = "asd1234"

girdimail= input("email:")
girdişifre = input("parola:")

kontrolmail= (email == girdimail.lower().strip())
kontrolsifre = (password == girdişifre.lower())
print("Email bilgisi doğru mu {0} ve şifre doğru mu {1}".format(kontrolmail,kontrolsifre))

#strip metoduyla sona veya başa gelen boşluklar silinir
"""
#Mantıksal Operatör
# and, or,not
#or => doğru doğru  doğru-  doğru yanlış  doğru
#not tamamen tersini alır.

#girilen sayının 0-100 arasında olup olmadığını kontrol edin
"""10.
a = float(input("sayı gir:"))
result = (a>0) and (a<=100)
print("Girilen sayı 0 ile 100 arasında mı: {0}".format(result))
"""
#girilen sayını pozitif çift sayı olup olmadığını kontrol
""" 11.
sayı = int(input("sayı gir: "))
result = (sayı>0) and (sayı %2 == 0)
print("Girdiğiniz sayı pozitif çift sayı mı ?: {0}".format(result))
"""
#kullanıcadan 2 vize(%60) ve final (%40) nnotunu alıp ortalama hesaplayınız
#ort 50nin üstündeyse geçti değilse kaldı
#a) ort 50 olsa bile final notu en az 50 olmalı
#b)finalden 70 alındığında ortun önemi yok

"""
vize1= float(input("1.vize:"))
vize2=float(input("2.vize:"))
final=float(input("final:"))
ortalama = ((vize1 + vize2)/2)*0.6 + (final*0.6)
result = (ortalama >= 50) or (final >=70)
print("öğrenci ortalaması : {0} ve geçme durumu {1}".format(ortalama,result))

"""
username = "hacerk"
password = "12345"

a = input("username:")
b = input("password:")

if(a == username):
    if(b == password):
        print("giriş başarılı")
    else:
        print("password hatalı")        
elif(a != username) and (b != password):
    print("password ve username hatalı")
else:
    print("username hatalı")
        














































































































