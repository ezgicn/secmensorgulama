# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:24:06 2020

@author: kaant
"""

print ('''
 SEÇMEN SORGULAMA SİSTEMİNE HOŞGELDİNİZ 

 [1] SEÇMEN KONTROL     
       
''')
yil=2020

islem=input("Yapmak İstediğiniz İşlemi Seçiniz : ");
if (islem=="1"):
    secmenAD=input("Adınızı Giriniz : ")
    secmenSOYAD=input("Soyadınızı Giriniz : ")
    secmenDOGUM=int(input("Doğum Yılınızı Giriniz : "))
    if (yil-secmenDOGUM < 18):
        print("OY KULLANAMAZSINIZ!")
    else:
        (yil-secmenDOGUM >= 18)
        print("OY KULLANABİLİRSİNİZ!")
        
    
    
    
