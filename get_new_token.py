#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import sys
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import logging
from subprocess import call

class Glovo_token:
    global bot_name, wd, login_path, browser, google_token, browser_log, sso_token, refresh_token, json_data
    bot_name  = "get_new_token"

    '''procedural code'''
    def __init__(self):
        #1:Set path
        Glovo_token.set_path()
        #Start logger
        Glovo_token.logger_start()
        #Check login data
        Glovo_token.first_login()
        #Launching browser
        Glovo_token.launch_Chrome()
        #Get google token
        Glovo_token.get_g_token()
        #Post google token
        Glovo_token.post_g_token()
        #Save token
        Glovo_token.save_token()
        
    '''Part 1: Access google account with selenium and get network requests'''
    '''Working directory and paths'''
    def set_path():
        global wd, login_path
        wd = os.getcwd()
        #defining paths
        login_path = os.path.join(wd,"my_personal_token.json")
    
    '''Logger'''
    #single logger, continously updating
    def logger_start():
        #log config
        logging.basicConfig(filename = "my_log.log", 
                        level =  logging.INFO,
                        format = "%(levelname)s %(asctime)s %(message)s",
                        datefmt = '%m/%d/%Y %H:%M:%S',
                        filemode = "a")
        #log start
        global logger
        logger = logging.getLogger()
        logger.info(f"Starting log for {bot_name}")
        print("logger started")
    
    '''Initiations functions'''
    def first_login():
        print(f"\n\nHello, you are about to get your new Admin access token.")
        time.sleep(2)
        print(f"\nYour token will be saved in a hidden file inside {os.path.basename(wd)} folder.")
        time.sleep(2)
        print("\nThe token is a personal key that identifies all your actions on Admin, therefore any usage of the bots is visible on Admin's log.")
        time.sleep(3)
        while True:
            time.sleep(1)
            print("\nFor starting, you will have to log into Admin:")
            global country
            country = input('Insert your country code (eg. IT, ES, AR):\n').upper().strip()
            global glovo_email
            glovo_email = input("Insert your glovo email:\n").strip()
            print(f"\nemail = {glovo_email}\ncountry = {country}")
            confirm = input("Confirm data? [yes]/[no]\n").lower().strip()
            if confirm in ["yes","y","ye","si"]:
                welcome_name = glovo_email[:glovo_email.find("@")].replace("."," ").title()
                print(f"\n\nWelcome {welcome_name}!\n\n")
                logger.info(f'Started by {welcome_name}')
                break
            else: continue
        #nprint('First login completed')
    '''
    def first_login_check():
        #Check/get login data
        print("Checking login data")
        if os.path.isfile(login_path):
            with open(login_path, 'r') as read_file:
                content = json.load(read_file)
            if all(s in content for s in ("glovo_email", "refresh_token", "country")):
                glovo_email = content['glovo_email']
                welcome_name = glovo_email[:glovo_email.find("@")].replace("."," ").title()
                print(f"\n\nWelcome back {welcome_name}!\n\n")
                logger.info(f'Started by {welcome_name}')
                confirm = input("Do you need to refresh your token or change your country setup? [yes]/[no]\n").lower().strip()
                if confirm not in ["yes","y","ye","si"]:
                    print('You can start using the bots then.\nFor lauching a bot simply double click on the bot you want to use.')
                    sys.exit(0)
            else: first_login()
        else:
            first_login()
    '''
    def launch_Chrome():
        time.sleep(2)
        print('Launching Chrome..')
        time.sleep(2)
        print('\nPlease enter your Glovo credentials and wait a few moments while bot gets you token.')
        global browser, wait
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        browser = webdriver.Chrome(desired_capabilities = caps, executable_path=ChromeDriverManager().install())
        browser.implicitly_wait(12)
        wait = WebDriverWait(browser, 600)
        Glovo_token.initiate_google_login()
        
    def initiate_google_login():
        global browser
        wait = WebDriverWait(browser, 600)
        browser.get("https://accounts.google.com/")
        print("\nAccessing your Google/Glovo account")
        time.sleep(10)
        wait.until(EC.title_is("Google Account"))
        logger.info('Logged with Google')
        time.sleep(1)
        print("Signed in!")
        browser.get("https://beta-admin.glovoapp.com/search")
        wait.until(EC.title_is("Glovo Admin"))
        time.sleep(10)
    
    '''Get google token from network log'''
    def get_g_token():  
        global google_token, browser_log, sso_token
        while True:
            time.sleep(1)
            browser_log = browser.get_log('performance')
            for i in browser_log:
                try:
                    sso_token = json.loads(json.loads(i['message'])['message']['params']['request']['postData'])['ssoToken']
                except Exception: continue
            try: sso_token
            except Exception: continue
            else: 
                logger.info(f'Got Sso Token: {sso_token}')
                browser.close()
                break
    '''
            for i in browser_log:
                try:
                    google_token = json.loads(json.loads(i['message'])['message']['params']['request']['postData'])['googleToken']
                except Exception:
                    continue
            try: google_token
            except Exception: continue
            else: 
                logger.info(f'Got Google Token: {google_token}')
                browser.close()
                break
    '''       
            
    '''Part2: Post google token to admin to get access key'''
    '''Send post request to admin api to receive access and refresh token'''
    def post_g_token():
        global refresh_token
        #define payload
        data = {'ssoToken': sso_token, 'grantType': "sso"}
        #POST request
        p = requests.post('https://adminapi.glovoapp.com/oauth/operator_token', json = data)
        logger.info('Posted sso Token at https://adminapi.glovoapp.com/oauth/operator_token')
        logger.info(f'Response is {p.ok}')
        refresh_token = p.json()['refreshToken']
        logger.info(f'Received Refresh Token: {refresh_token}')
    
    def save_token():
        global json_data
        json_data = {'glovo_email' : glovo_email,
                     'refresh_token' : refresh_token,
                     'country' : country}
        with open(login_path, "w") as dst_file:
            json.dump(json_data, dst_file)
        if 'TERM_PROGRAM' in os.environ:
            platform = 'mac'
        else:
            platform = 'windows'
        if platform == 'mac':
            call(["chflags", "hidden", login_path])
        elif platform == 'windows':
            call(["attrib", "+h", login_path])
        print(f'\n\nCongrats!\nYour Refresh Token has been saved to {login_path}.')
    
    
