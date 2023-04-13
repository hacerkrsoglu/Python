# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 23:40:49 2023

@author: Hacer
"""
"""
# 1.Soru

def reverse(s):
    islem = (s[::-1])
    print(islem)
reverse('happy')   
reverse('Python') 
reverse("") 
reverse("P")  
"""

"""
# 2.Soru
def mirror(s):
    islem = (s+s[::-1])
    print(islem)
mirror("good")
mirror("yes")
mirror("Python")
mirror("")
mirror("a")
"""
"""

#3.Soru
def remove_letter(letter,strng):
    for i in strng:
        if(i == letter):
            continue
        print(i)   
remove_letter("i", "Mississippi")  
print("****************")    
remove_letter("a", "apple")  
print("****************")
remove_letter("z", "banana")  
print("****************")
remove_letter("a", "banana")  
print("****************")
"""
"""
#4.Soru
def is_palindrome(s):
    if(s == s[::-1]):
        print("True")
    else:
        print("False")
is_palindrome("abba")        
is_palindrome("abab")  
is_palindrome("tenet")  
is_palindrome("banana")  
is_palindrome("straw warts")  
"""
"""
#5.Soru
def count(sub,s):
    islem = s.count(sub)
    print(islem)

count("an","banana")
count("is","Mississippi")
count("ana","banana")
count("nana","banana")
count("nanan","banana")
"""
"""
 bunun çıktısı daha güzel
def remove_all(sub,s):
    
    islem = s.replace(sub,"")
    print(islem)
   
remove_all("iss", "Mississippi")
remove_all("cyc", "bicycle")
remove_all("an", "banana")
remove_all("eggs", "bicycle")

"""

"""
def remove_all(sub,s):
    
    while sub in s:
        islem = s.replace(sub, "")
        break
    print(islem)
   
remove_all("iss", "Mississippi")
remove_all("cyc", "bicycle")
remove_all("an", "banana")
remove_all("eggs", "bicycle")
"""


"""
def remove(sub,s):
    
   if sub in s:
         islem = s.replace(sub, '', 1)
         print(islem)
   else:
        print(s)
remove("an", "banana")
remove("cyc", "bicycle")
remove("iss", "Mississippi")
remove("egg", "bicycle")
"""
