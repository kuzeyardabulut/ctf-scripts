#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
hedefip = input("Ip Address: ")
os.system("apt-get install figlet")
os.system("apt-get install knockpy")
os.system("apt-get install gobuster")
os.system("apt-get install nikto")
os.system("apt-get install nmap")
os.system("clear")
os.system("figlet NMAP")
print("""


""")
os.system("nmap -sV " + hedefip + " -T4 --script=vuln")
print("""


""")
os.system("figlet GOBUSTER")
print("""


""")
os.system("gobuster dir -u http://" + hedefip + " -w /usr/share/dirb/wordlists/common.txt")
print("""


""")
os.system("figlet KNOCKPY")
print("""


""")
os.system("knockpy " + hedefip)
print("""


""")
os.system("figlet NIKTO")
print("""


""")
os.system("nikto -h " + hedefip)
