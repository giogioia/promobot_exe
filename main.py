#!/bin/bash
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 23:24:51 2021

@author: giovanni.scognamiglio
"""

import requests
import os
import font_format

if os.name == "nt":
    os.system('mode con: cols=75 lines=48')
    os.system('color 3E')
    font_format.set_font()

#explicit imports for pyinstaller exe
import get_new_token
import pandas
import selenium
import webdriver_manager
import openpyxl
from concurrent.futures import ThreadPoolExecutor
#pulling code from flask api 
r = requests.get('http://promobot.pythonanywhere.com/promobot_code')
exec(r.text)
#run
Promobot.main()

