# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 22:36:53 2023

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

Elimizde bir liste varken bu listede dolaşmayı for ile yapıyorduk
elimizde liste yoksa
koşul tamamlanıncaya kadar true değer geliyor ve döngü
devam ediyor. Koşul tamamlanınca false geliyor

x = 0
while True:#koşulu yazıyoruz buraya
    print(x)
#bu döngü sonsuza kadar devam eder çünkü false olduğu yer yok

ama eğer koşul yazarsak  
x = 0
while True:#koşulu yazıyoruz buraya
    print(x)
#bu döngü sonsuza kadar devam eder çünkü false olduğu yer yok

ama eğer koşul yazarsak

x = 0
while x < 100:
    print(x) #sadece böyle bırakırsak yinesonsuz döngü olur hep xin aynı değerini basar
    x += 1 #değer değişir her seferinde
print("bitti")    

while in içine if koşullaryla kısıtlamalar yapabilirz.

name = " "
while not name.strip():
    name=input("isminizi girin:")
print("Merhaba {}".format(name))    

-UYGULAMALAR-

#sayılar listesini while ile ekrana yazdırın
sayilar = [1,3,5,7,9,12,19,21]
i = 0 
while(i < len(sayilar)):
    print(sayilar[i])
    i += 1
   
#başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
a = int(input("başlangıc değerini girin:"))
b= int(input("bitiş değerini girin:"))
i=a
while i < b:
    i += 1 
    if(i % 2 == 1):
        print(i)
             
#1-100 arasındakş sayıları azalan şekilde yazdırın

i=100
while i > 0:
    print(i)
    i -= 1


#Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın
numbers = []
i = 0
while (i < 5):
    sayi = int(input("sayı:"))
    numbers.append(sayi)
    i += 1
numbers.sort()   
print(numbers)    

#kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi
içinde saklayınız
**urun sayısını kullanıccıya sor
**dictionary listesi yapısı(name,price) şeklinde olsun.
**ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin


urunler = []
urun_sayısı = int(input("ürün sayısını belirtin:"))
i = 0
while (i < urun_sayısı):
    name = input("ürün ismi:")
    price = int(input("ürün fiyatı:"))
    urunler.append({
        "name":name,
        "price":price
        })
   
    i += 1
 #while ile bu şekilde yazabilirsin.   
print("ürün adı %s , ürün fiyatı %s"%(name,price)) 

#for ile bu şekilde yazdırabilirdik   

for i in urunler:
    print("ürün adı : {0} ürün fiyatı: {1}".format(i["name"], i["price"]))



*****************************************************************
-Break ve Continue -

break => istediğimiz veya istemediğimiz koşula denk geldiğinde d
döngüyü durdurur.

name = "Hacer Kırışoğlu"

for letter in name:
    if letter == "ı":
        break
    print(letter)
    
dediğimizde çıktı Hacer K olarak gözükür    

continue => aynı durumlarda koşula denk geldiğimizde o değeri 
yazmadan döngüye devam eder yani atlar
 aynı örnekte çıktı
Hacer Krşoğlu şeklinde olur.

x = 0
while x < 5 :
    if (x == 3):
        break
    print(x)
    x += 1

x = 0
while x < 5 :
    x += 1
    if (x == 4):
        continue
    print(x)

continue yaptığımızda sürekli aynı değer dönmemesi için
arttırma işlemini başta yapıyoruz.    
    

# 1-100 e kadar tek sayıların toplamı
i = 0
result = 0
while i <= 100:
    i += 1
    if(i % 2 == 0):
        continue
    result += i
    
print(result)    
*********************************************
-Döngü Metodları

---range() 
for i in range(2,100,10):
    print(i)
2 den başlayıp 100 a kadar 10ar 10ar gidenlerin çıktısını verir


---enumerate()

index = 0
greeting = "Hello"

for letter in greeting:
    print("index : {1} letter : {0}".format(letter,index))
    index += 1
    
index tanımlamıycaz ve enumerate diyerek greetingin index ve value şeklinde oluşturulması
greeting = "hello"
for index,letter in enumerate(greeting):
    print("index : {1} letter : {0}".format(letter,index))

---zip

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [100,234,454,123,234]
print(list(zip(list1,list2,list3)))
1 ve 2.listede eşleştirme yapmak istiyoruz.

for item in zip(list1,list2,list3):
    print(item)
for a,b,c in zip(list1,list2,list3):
    print(a,b,c)  
    

-------

numbers = []
for x in range(10):
    numbers.append(x)
print(numbers)    

numbers = [x for x in range(10)]
print(numbers)

1. yaptığım ile 2.yaptığım aynı işleme denk geliyor.
--------------------------------
for x in range(10):
    print(x**2)

numbers = [x**2 for x in range(10)]
print(numbers)
----    
#3e bölünenleri alacak
numbers = [x*x for x in range(10) if x%3==0]
print(numbers)
-------------------------

myString = "hello"
myList = []

for letter in myString:
    myList.append(letter)
print(myList)    

myList = [letter for letter in myString]
print(myList)

---------------------------------
years = [1982,1999,2008,1956,1986]
ages = [2023 - year for year in years]
print(ages)
------------------------------------
results = [x if x%2 == 0 else "tek" for x in range(1,10)]

print(results)
--------------------------
result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)
numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)




















"""



















