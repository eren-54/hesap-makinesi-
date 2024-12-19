# BASİT HESAP MAKİNESİ
import numpy as np
try:
    sayı1 = float(input("sayı 1 i giriniz: "))  # Girilen değeri float'a dönüştürme
    sayı2 = float(input("sayı 2 yi giriniz: "))

    hesaplama_işlemi = input("İşlem giriniz (+, -, /, *): ")

    if hesaplama_işlemi == "+":
        print(sayı1 + sayı2)
    elif hesaplama_işlemi == "-":
        print(sayı1 - sayı2)
    elif hesaplama_işlemi == "/":
        print(sayı1 / sayı2)
    elif hesaplama_işlemi == "*":
        print(sayı1 * sayı2)
    else:
        print("Geçersiz işlem. Lütfen +, -, / veya * giriniz.")
except ZeroDivisionError:
    print("Bir sayıyı sıfıra bölemezsiniz! Lütfen tekrar deneyin.")