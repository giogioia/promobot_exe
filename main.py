#!/bin/bash
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 23:24:51 2021

@author: giovanni.scognamiglio
"""

import get_new_token
import requests
import pandas
import selenium
import webdriver_manager
import openpyxl
import os
import font_format
from concurrent.futures import ThreadPoolExecutor

if os.name == "nt":
    os.system('mode con: cols=75 lines=48')
    os.system('color 3E')
    font_format.set_font()
r = requests.get('http://promobot.pythonanywhere.com/promobot_code')
exec(r.text)
Promobot.main()

