# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 23:20:51 2023

@author: Hacer
"""


"""
soru 1
Bir kelimenin içerisindeki karakterlerin soldan sağa alfabetik sıraya göre dizilip
dizilmediğini kontrol eden bir fonksiyon yazınız. Fonksiyona “alfabetik_artan”
ismini veriniz. Fonksiyon parametre olarak bir kelime almalı, geri dönüş değeri 
olarak boolean türünde True (sözcüğün alfabetik olarak dizildiği durumlar için) 
ya da False (diğer durumlar için) döndürmelidir. Fonksiyona sadece küçük harflerden 
oluşan ve Türkçe harf içermeyen kelimeler girilmelidir. 



print("Gireceğini kelime küçük harfle başlamalı\nve Türkçe harf içermemelidir. ")
def alfabetik_artan(kelime):
    
    for i in kelime:
        if("ç" in kelime):
            print("Türkçe karakter bulunmayan kelime girin")
            break
        elif("ğ" in kelime):    
            print("Türkçe karakter bulunmayan kelime girin")
            break
        elif("ı" in kelime):    
            print("Türkçe karakter bulunmayan kelime girin")
            break
        elif("ö" in kelime):    
            print("Türkçe karakter bulunmayan kelime girin")  
            break
        elif("ü" in kelime):    
            print("Türkçe karakter bulunmayan kelime girin")
            break
        elif("ş" in kelime):    
            print("Türkçe karakter bulunmayan kelime girin")  
            break
        else:
            if (kelime.isalpha() and kelime.islower()):
                islem = ''.join(sorted(kelime))
                print("girilen kelime : {0}, sıralanmış hali : {1}".format(kelime, islem))
                if(kelime == islem):
                    return True
                else:
                    return False
    
        
print(alfabetik_artan("adem"))
print(alfabetik_artan("koop"))
print(alfabetik_artan("kaan"))
print(alfabetik_artan("emre"))         

"""
"""
soru 2
Parametre olarak bir liste alan ve sonuç olarak ekrana, bu listenin 
elemanlarından kaçının karakter dizisi, kaçının tamsayı, kaçının ondalıklı
sayı, kaçının “boolean”, kaçının liste olduğunu yazan, geri dönüş değeri
döndürmeyen bir fonksiyon yazınız. Fonksiyonunuza “Liste_anaLizi” ismini veriniz. 
Fonksiyonun, parametre olarak verilen listenin içinde eleman olarak bulunan 
diğer listelerin içerikleriyle ilgilenmesine lüzum yoktur. 


def liste_Analizi(liste):
    karakter_dizisi = 0
    tam_sayi = 0
    ondalikli_sayi = 0
    boolean = 0
    liste_turu = 0
    
    for eleman in liste:
        if type(eleman) == str:
            karakter_dizisi += 1
        elif type(eleman) == int:
            tam_sayi += 1
        elif type(eleman) == float:
            ondalikli_sayi += 1
        elif type(eleman) == bool:
            boolean += 1
        elif type(eleman) == list:
            liste_turu += 1
    
    print("Karakter Dizisi Sayısı:", karakter_dizisi)
    print("Tam Sayı Sayısı:", tam_sayi)
    print("Ondalıklı Sayı Sayısı:", ondalikli_sayi)
    print("Boolean Sayısı:", boolean)
    print("Liste Sayısı:", liste_turu)

print(liste_Analizi(["H2O",18,0,100.0,"Bileşik","Kovalent",["Hidrojen",2],["Oksijen",1,3],True]))


"""











        