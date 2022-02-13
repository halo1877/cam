import os, wget
import sys
import time
import requests
os.system('clear')
os.system('rm -rf shk.txt')
os.system('id -u > shk.txt')
uidd = open('shk.txt', 'r')
for j in uidd:
    sp = j.split()
    

def X():
    logo = ''' \n
\n'''
    uuid = str(os.geteuid()) + str(os.getlogin())
    id1 = uuid
    id = (id1).join(uuid)
    print ('\x1b[37;1m YOUR ID : ' + id)
    http = requests.get('https://raw.githubusercontent.com/malatool/palabunim/main/list.txt').text
    if id in http:
            print ('\x1b[92mYOUR ID IS ACTIVE.........')
            msg = str(os.geteuid())
            time.sleep(1)
    else:
            print ('\x1b[91m id active nya HOW bo active krdn: @mala_bek4s >.......')
            time.sleep(2)
            print (logo)
            sys.exit()
            X()
X()

print("\033[1;92m ")
logo='''

____       _       _
|  _ \ __ _| | __ _| |__  _   _ _ __
| |_) / _` | |/ _` | '_ \| | | | '_ \
|  __/ (_| | | (_| | |_) | |_| | | | |
|_|   \__,_|_|\__,_|_.__/ \__,_|_| |_|


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[1;97m
  Author   : Omar Palabun.
  Chanal Tlegram : @itsmepalabun
  Telegram : @I4m_palabun
  Nrx:10$
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1 = Checker Facbook ID vip
2 = Checker Facbook Number 
3 = Checker Inistagram
4 = Cheker Twitar Vip
5 = Drust kerni Combo Vip
6 = spam bot
7 = report instagram

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
print(logo)
def dwbara():
        chs=raw_input("halbzhera : ")
        if chs=='1':
                wget.download("https://raw.githubusercontent.com/malatool/idfacbook.py/main/idfacbook.py")
                os.system("python2 idfacbook.py")
        elif chs=='2':
                wget.download("https://raw.githubusercontent.com/malatool/fbnumber/main/fbnumber.py")
                os.system("python2 fbnumber.py")
        elif chs=='3':
                wget.download("https://raw.githubusercontent.com/malatool/instaaa/main/instaaa.py")
                os.system("python instaaa.py")
        elif chs=='4':
                wget.download("https://raw.githubusercontent.com/malatool/palabunim/main/palabunim.py")
                os.system("python palabunim.py")
        elif chs=='5':
                wget.download("https://raw.githubusercontent.com/malatool/shude/main/Shude.py")       
                os.system("python Shude.py")
        elif chs=='6':
                wget.download("https://raw.githubusercontent.com/malatool/spambot/main/spambot.py")       
                os.system("python spambot.py") 
        elif chs=='7':
                wget.download("https://raw.githubusercontent.com/malatool/repinsta/main/repinsta.py")       
                os.system("python repinsta.py")  
        else:
                print(" Aw zhmaray Tya nya !")
                dwbara()
dwbara()