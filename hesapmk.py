
from os import system
import pyautogui as pg
import time 
from colorama import Fore

class HesapMakinesi:
    

    def wp():
        try:
            while True:
                a=int(input("""
Whatsapp bomb = 1
SMS bomb = 2
Çıkış = 3
                            
Seçim : 
"""))
            
                if a == 1:

                    mes=input("Göndermek istediğiniz mesajı giriniz: ")
                    adet=int(input("Kaç tane göndermek istiyorsunuz: "))
                    t=int(input("Kaç saniye aralıkla göndermek istersiniz: "))
                    time.sleep(5)
                    for i in range(adet):
                        time.sleep(t)
                        pg.write(mes)
                        pg.press("Enter")
                
                
                elif a ==2:
                    import enough 









                elif a ==3:
                    system("cls||clear")
                    pg.hotkey('ctrl', 'c')
        except KeyboardInterrupt:
            system("cls||clear")
            
            print(Fore.LIGHTYELLOW_EX,"Çıkış yapılıyor...")
                    

            
                

            
        

    

    def topla(a,b):
        return a+b
    
    def cıkar(a,b):
        return a-b
    
    def capr(a,b):
        return a*b
    
    def bol(a,b):
        return a/b
    

    while True:
        print(" ")
        opt=int(input("""
Hesap Makinesi
----------------------
1 = Toplama
2 = Çıkarma
3 = Çarpma
4 = Bölme
----------------------

Seçim: """))
            
        
        if opt>5:
            print("Hatalı tuşlama...")
            system("cls||clear")
            break
        
        if opt==5:
            print(Fore.LIGHTRED_EX)
            print("Gizli Mod Açıldı...")

            print(" ")

            wp()
            break
        else:

            a=int(input("Birinci sayıyı giriniz: "))
            b=int(input("İkinci sayıyı giriniz: "))

            if opt == 1:
                print("Sonuç = ",topla(a,b))
                
                break

            elif opt == 2:
                print("Sonuç = ",cıkar(a,b))
                
                break

            elif opt == 3:
                print("Sonuç = ",capr(a,b))
                
                break

            elif opt == 4:
                print("Sonuç = ",bol(a,b))
                
                break
                
            


        
        