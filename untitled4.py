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
        
"""
"""
#ehliyet alabilme durmu

name = input("isminiz: ")
education = input("eğitim durumunuz: ")
age = int(input("yaşınız:"))
if (age >= 18)  :
    if((education == "lise" or education == "üniversite")):
        print("Ehliyet alabilirsiniz.")
    else:
        print("ehliyet alamazsınız eğitim durumunuz tutmuyor.")
else:
    print("ehliyet alamazsınız yaşınız tutmuyor ")
    
"""
"""
#Hesap Makinesi

print("işlem Bilgilendirmesi\n 1.işlem = Toplama\n 2.İşlem = Çıkarma\n 3.İşlem= Çarpma\n 4.İşlem=Bölme")

islem = int(input("işlem seçiniz:"))
sayı1= int(input("1.sayıyı girin:"))
sayı2=int(input("2.sayıyı girin:"))

if islem == 1:
    print("{0} ile {1} toplamı:{2}".format(sayı1,sayı2,(sayı1 + sayı2)))
elif islem ==2:
    print("{0} ile {1} farkı:{2}".format(sayı1,sayı2,(sayı1 - sayı2)))
elif islem ==3:
    print("{0} ile {1} çarpımı:{2}".format(sayı1,sayı2,(sayı1 * sayı2)))    
elif islem ==3:
    print("{0} ile {1} bölümü:{2}".format(sayı1,sayı2,(sayı1 / sayı2)))
else:
    print("geçerli bir işlem seçiniz")

"""

"""
# is

x = [1,2,3]
y = [2,4]

print(x is y) # aynı objecler mi diye sorar false döner.

del x[2] = xin 2.indeksini siler.
 
reverse fonksiyonu =
listenin içerdiği verileri sorasıyla tam tersine çevirir.


# in
x= ['apple','banana']
print('banana' in x)
true döner = içinde var mı anlamına gelir
replace('w','W') değiştirme metodu


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





























































































































