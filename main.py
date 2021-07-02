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

def call_PromoBot():
    global PromoBot
    r = requests.get('https://el-promobot.netlify.app/code.py')
    with open(os.path.join(os.getcwd(),'temp_module.py'),'w+') as file:
        file.write(r.text)
    # from temp_module import Promobot
    temp_module = SourceFileLoader("temp_module.py", os.path.join(os.getcwd(),'temp_module.py')).load_module()   
    PromoBot = temp_module.PromoBot
    os.remove(os.path.join(os.getcwd(),'temp_module.py'))

if __name__=='__main__':
    set_background()
    call_PromoBot()
    PromoBot.exe_checker(exe_version)
    PromoBot.driver()

