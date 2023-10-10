# -*- coding: utf-8 -*-
"""
Created on Mon May 22 22:51:10 2023

@author: Hp
"""

from selenium import webdriver
import os
from time import sleep
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\Hp\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_experimental_option("detach", True)
options.add_argument('--profile-directory=Profile 2')

url= "https://www.instagram.com/direct/inbox/"
master_username= "if_i_were_true_abt_u"
password= "$Pq12345678"
#########################################################################################
       
driver = webdriver.Chrome(executable_path="E:\\c data\\Desktop\\operation63\\chromedriver.exe",chrome_options=options)
driver.get(url)
time.sleep(5)


#clicking on "log in" button
Sumbit= driver.find_element(By.XPATH,"//*[contains(text(), 'Log In')]")
Sumbit.click()


#entering user_id
user_name=WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.NAME, 'username')))
user_name.send_keys(master_username)


#entering password
user_pass=WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.NAME, 'password')))
user_pass.send_keys(password)


#clicking on "log in" button
Sumbit= driver.find_element(By.XPATH,"//*[contains(text(), 'Log in')]")
Sumbit.click()
time.sleep(5)

#removing first two pop-ups (restore and notifications)
if driver.find_element(By.CLASS_NAME,'_ac8f'):
    driver.find_element(By.CLASS_NAME,'_ac8f').click()

if driver.find_element(By.CLASS_NAME,'_a9-z'):
    driver.find_element(By.CLASS_NAME,'_a9-z').click()
time.sleep(5)

#clicking message button
driver.find_element(By.XPATH,"//*[contains(text(), 'Message')]").click()
