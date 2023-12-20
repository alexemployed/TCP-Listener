#! /usr/bin/python3

# Coding: UTF-8
# Name: TCP-Listener
# Author: AlexEmployed
# Version: 0.0.1
# License: GPL-3.0 version
# Copyright: alexemployed 2023
# Github: https://github.com/alexemployed
# Language: Python


# Imports
import sys
import os
import asyncio
import platform

# Colors
_black = "\033[0;30m"
_red = "\033[0;31m"
_green = "\033[0;32m"
_brown = "\033[0;33m"
_blue = "\033[0;34m"
_yellow = "\033[1;33m"
_purple = "\033[0;35m"
_cyan = "\033[0;36m"
_white="\033[0;37m"
_lightGray = "\033[0;37m"
_darkGray = "\033[1;30m"
_lightRed = "\033[1;31m"
_lightGreen = "\033[1;32m"
_lightBlue = "\033[1;34m"
_lightPurple = "\033[1;35m"
_lightCyan = "\033[1;36m"
_lightWhite = "\033[1;37m"


# Privalages
os_name = platform.system()
    
def check_root():
    return os.geteuid() == 0

def check_admin():
    if os.name == 'nt':
        try:
            temp = os.listdir(os.sep.join([os.environ.get('SystemRoot', 'C:\\Windows'), 'temp']))
        except:
            return (os.environ['USERNAME'], False)
        else:
            return (os.environ['USERNAME'], True)
    else:
        if 'SUDO_USER' in os.environ and os.geteuid() == 0:
            return (os.environ['SUDO_USER'], True)
        else:
            return (os.environ['USERNAME'], False)
        

# Functions
async def scan_port(ip, port):
    try:
        reader, writer = await asyncio.open_connection(ip, port)
        print(f"{_green}[+]{_white} {_darkGray}{ip}{_white}:{_green}{port}{_white} is {_green}OPEN{_white}")
        log_txt = f"{host}:{port} is OPEN!\n"
        with open('logs.txt', 'a+') as file: 
            file.write(log_txt)
        
        writer.close()
    except:
        pass

async def scan_ports(ip):
    tasks = [scan_port(ip, port) for port in range(1, 1024)]
    await asyncio.gather(*tasks)

# Get the host from the user
host = input(f"{_yellow}[!]{_white} Enter the host: ")


if __name__ == '__main__':
    try:
        asyncio.run(scan_ports(host))
    except KeyboardInterrupt:
        print(f"Program {_red}end{_white} by user!")
        sys.exit(0)
