#!/bin/bash
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 23:24:51 2021

@author: giovanni.scognamiglio
"""

import requests
import os
import font_format
from importlib.machinery import SourceFileLoader
import sys

#explicit imports for pyinstaller exe
import get_new_token
import pandas
import selenium
import webdriver_manager
import openpyxl
import regex

exe_version = 1.1

def set_background():
    if os.name == "nt":
        os.system('mode con: cols=75 lines=48')
        os.system('color 3E')
        font_format.set_font()

def call_promobot():
    global Promobot
    r = requests.get('https://el-promobot.netlify.app/code.py')
    with open(os.path.join(os.getcwd(),'temp_module.py'),'w+') as file:
        file.write(r.text)
    # from temp_module import Promobot
    temp_module = SourceFileLoader("temp_module.py", os.path.join(os.getcwd(),'temp_module.py')).load_module()   
    Promobot = temp_module.Promobot
    os.remove(os.path.join(os.getcwd(),'temp_module.py'))

def check_version():
    exe_version_needed = Promobot.exe_version()
    if exe_version != exe_version_needed:
        conf = input('A new executor is available. Download new version? [yes/no]\t')
        if conf in ['yes','ye','y','si']:
            print('Estimated time: ~60 seconds.\nDownload in progress... Do not close the terminal page.')
            try:
                r = requests.get('https://el-promobot.netlify.app/assets/PromoBot.exe')
                with open('PromoBot.exe', 'wb') as file:
                    file.write(r.content)
            except Exception:
                print('Something went wrong.\nTry downloading new bot manually from https://el-promobot.netlify.app/')
                k=input('\nPress Enter x2 to close')
                sys.exit(0)
            else: 
                print('\nNew PromoBot.exe successfully downloaded!\nClose this window and lanch Promobot.exe again')
                k=input('\nPress Enter x2 to close')

if __name__=='__main__':
    set_background()
    call_promobot()
    check_version()
    Promobot.driver()

