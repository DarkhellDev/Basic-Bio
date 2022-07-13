from multiprocessing.connection import wait
import sys
from gevent import sleep
if sys.platform == 'win32':
    try:
        from colorama import Fore, init
        init()
    except ImportError: 
        pass 
from lazyme.string import color_print
import time

def logo():
	color_print("""
 +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
 |D|a|r|k|h|e|l|l|'|s| |S|e|r|v|i|c|e|s|
 +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+


  ================================
                MENU
  ================================
  1 - Darkhell's Services Discord invite
  2 - Debug Entity Discord invite
  3 - Personal Discord
  4 - Exit
  ================================
""", color='blue')


logo()
count = 0

ans=True
while ans:
    ans= input("Enter Your option : ") 
    if ans=="1": 
      color_print('Here`s my discord Server : https://discord.gg/My8PkSAjG5', color='blue') 
    elif ans=="2":
      color_print('Debug Entity Team : https://discord.gg/VKEafKrGsB', color='green')
    elif ans=="3":
      color_print('Feel free to DM me : Darkhell#0001', color='yellow')
    elif ans=="4":
      color_print('Quiting 1%', color='red')
      time.sleep(0.2)
      color_print('Quiting 20%', color='yellow')
      time.sleep(0.2)
      color_print('Quiting 30%', color='pink')
      time.sleep(0.3)
      color_print('Quiting 40%', color='blue')
      time.sleep(0.2)
      color_print('Quiting 50%', color='green')
      time.sleep(0.4)
      color_print('Quiting 60%', color='red')
      time.sleep(0.2)
      color_print('Quiting 70%', color='yellow')
      time.sleep(0.1)
      color_print('Quiting 80%', color='pink')
      time.sleep(0.1)
      color_print('Quiting 90%', color='blue')
      time.sleep(0.5)
      color_print('Quiting 100%', color='red')

      time.sleep(2.0)

      quit()
    elif ans !="":
      color_print("\n Not Valid Choice Try again", color='red') 
