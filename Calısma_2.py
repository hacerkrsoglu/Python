# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 22:07:02 2023

@author: Hacer
"""

"""
*****************************************
 String metodlaarı
upper() metodu = karakterleri büyük harfe çevirir hepsini
lower() = hepsi küçük olur
title() = her kelimenin  baş harfini büyük yapar
capitalize() = girilenin ilk kelimesinin baş harfini büyük yapar
strip() = baş ve sondaki boşluklar gider sağdaki silmek istersek rstrip() lstrip()
split() = girilen ifade boşluk ifadelerine göre bölünür ve ayrı ayrı liste olarak aır
join() = splitte ayrılanları birleştirir ' '.join() dersek araya boşluk koyarak birleştirir
find() = verilen ifadenin içinde var mı o diyerek arama yapar
startswith('H')=verilen ifade H ile mi başlıyor
center() = verilen ifadeyi 100 karakterlik içine alır.
count('a') = gibi ifade girdiğimiz ifadenin içinde kaç tane a old. gösterir.
isalpha() = içindeki ifadeler alfabetik mi
isdigit() = gelen değerlr rakam veya decimal mi

********************************************
Listeler
my_list= [içine istenileen türde ifade yazabiliriz.]
iki listeyi + ile tek liste şeklinde ekleyebiliriz.
listenin eleman sayısına len() ile ulaşabiliriz

in operatörü içinde mi? anlamı
arabalar = ["mercedes"]
result = "mercedes" in arabalar

lisstenin üzerine eleman eklemek için .append() sona ekler
istediğimz konuma ekleme yapmak için .insert(önce index bilgisis,sonra eklenecek olan)
eleman silmek için .pop() sondaki silinir içine index vererek istediğimiz silebiliriz.
.remove()metodunda içine silme istediğimiz değeri veriyoruz.
.sort() liste sayısal büyüklük olarak sıralanır veya alfabatik
.reverse diyerek listeyi tam tersine çevirebilirz.
.count() istediğimiz elamanı saydırabiliriz.
.clear() siler her şeyi
.index() deyip içine index numarasını istediğimiz ifadeyi yazariz ve hangi indexte old. öğreniriz.

elemanları ters çevirme [::-1]
min(),max()
*********************************************
Tuple

list = [1,2,3] tipi list
tuple = (1,"iki,3") tipi tuple

indexlerine ulaşabiliriz ikisininde
eklemeler yapabiliriz
tuple da herhangi bir elemana atama yapamayız
tuple[0] = "deniz" gibi yapamayız
tek bir eleman üzerinde değişime izin vermiyor.
.count()
.index() 
*************************************
Dictionary
key - value şeklinde 

sehirler = ["kocaeli", "istanbul"]
plaka = [41,34]
print(plaka[sehirler.index("kocaeli")])
41 çıktısını verir

bunu dic'le
plakalar = {"kocaeli": 41, "istanbul": 34}
print(plakalar["kocaeli"])
çıktı 41
plakalar["ankara"] = 6 dediğimizde eklenme olur
*******************************************
Sets
fruits = {"orange"","apple"}
print(fruits)
index değerlerine ulaşamayız indexlenemez bir liste
sıralama yapamayız
.add ile yeni eleman ekleyebiliriz
fruits.add("banana")
.update() ile liste gönderebilriz
fruits.update(["mango","grape"]) 
eğer zaten içinde olan bir elamanı da eklemiş olsaydık aynı olan dğerler içerde saklanmazdı
ve en sona sadece 1 tane olacak şekilde ekleniri.
.remove("apple") sieriz
.discaard("apple")silerizz
.pop() herhangi bir eleman olabilir silinen eleman
.clear() bütün elemandar silinir
****************************************
Value and Referance

value typler bellekte farklı adreslerde tutulurlar
yapılan değişiklik birbirinden bağımsız olur
string number (float int )değerler

referance
list,class
aynı şekilde değişim gösterirler

"""