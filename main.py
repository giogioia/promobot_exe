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
import colorama
import xlrd
r = requests.get('http://promobot.pythonanywhere.com/promobot_code')
r.text
exec(r.text)
Promobot.main()

