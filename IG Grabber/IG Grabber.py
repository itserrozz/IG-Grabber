import requests
import time
import os
from colorama import Fore , init, Style
init()
num=0
cls=lambda :os.system('cls')
HEADERS={'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Accept': "*/*",'Host': 'www.instagram.com'}
user_list = open("usernames.txt", "w")
keyword=open("keywords.txt","r").read().splitlines()
def grab(sleep):
    global num
    try:
        for word in keyword:
            time.sleep(int(sleep))
            url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="
            response = requests.get(url + word + "&count=1800", headers=HEADERS).json()
            for index in response['users']:
                username = index['user']['username']
                num += 1
                print(username)
                user_list.write(f"{username}\n")
        user_list.close()
        cls()
        input(f"[!] Total Usernames : {num}")
        exit(0)
    except Exception:
        print('[-] Error ==> ')


print(f'''{Fore.CYAN}
██╗░██████╗░   ░██████╗░██████╗░░█████╗░██████╗░██████╗░███████╗██████╗░
██║██╔════╝░   ██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║██║░░██╗░   ██║░░██╗░██████╔╝███████║██████╦╝██████╦╝█████╗░░██████╔╝
██║██║░░╚██╗   ██║░░╚██╗██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝░░██╔══██╗
██║╚██████╔╝   ╚██████╔╝██║░░██║██║░░██║██████╦╝██████╦╝███████╗██║░░██║
╚═╝░╚═════╝░   ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝{Style.RESET_ALL}\n==================Codded By @404.erroz===============''')
slp=input("[+] Sleep (sec) : ")
grab(slp)
