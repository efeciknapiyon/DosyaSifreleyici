import pyAesCrypt
import os
import time


bufferSize = 64 * 1024
os.system("cls")
while True:
    print ("""
1) Şifreleme
2) Şifre çözme
""")
    secim = input("İşlem : ")
    
    if secim == "1":
        dosya = input("Dosya: ") 
        passs = input("Şifre : ") 
        pyAesCrypt.encryptFile(dosya, dosya+".aes", passs, bufferSize)
        print("Tamamlandı") 
        time.sleep(1) 
        os.system("cls") 
    

    elif secim == "2":
        dosya = input("Dosya: ") 
        passs = input("Şifre : ") 
        uzanti = dosya[:-4] 
        pyAesCrypt.decryptFile(dosya, "out"+uzanti, passs, bufferSize)     
        print("Tamamlandı!") 
        time.sleep(1) 
        os.system("cls")
        print(Bu Uygulama Efe ÇINAR tarafından kodlanmıştır.)