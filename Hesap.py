
from os import system
from colorama import Fore, Style
import pyautogui as pg
import time 

system("cls||clear")

print(Fore.LIGHTYELLOW_EX,"""
   ____   _   _  __     __ __     __     _      ____  
  / ___| | | | | \ \   / / \ \   / /    / \    / ___| 
 | |     | |_| |  \ \ / /   \ \ / /    / _ \   \___ \ 
 | |___  |  _  |   \ V /     \ V /    / ___ \   ___) |
  \____| |_| |_|    \_/       \_/    /_/   \_\ |____/ 

                                                    
""",Style.RESET_ALL)




print(Fore.LIGHTCYAN_EX)
kullanıcı="ebaki"
sifre="emir"
say=0

while True:
    kadi=input("Kullanıcı adınızı giriniz : ")
    sif=input("Şifrenizi giriniz : ")


    
    if kadi == kullanıcı and sif == sifre:
            print(" ")
            print(Fore.GREEN)
            print("Sisteme hoşgeldiniz.")
            print(Fore.LIGHTGREEN_EX)
            
            from hesapmk import HesapMakinesi as hs
            break
    else:
            print("Bilgileriniz yanlış...")
            print(" ")
            say+=1
            if say ==3:
                   print("Hesap Kilitlendi.")
                   system("cls||clear")
                   break





