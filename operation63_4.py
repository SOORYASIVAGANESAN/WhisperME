
  
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 09:30:11 2023

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
from selenium.common.exceptions import NoSuchElementException

time.sleep(5)
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\Hp\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_experimental_option("detach", True)
options.add_argument('--profile-directory=Profile 2')


url= "https://www.instagram.com/direct/inbox/"
master_username= "if_i_were_true_abt_u"
password= "$Pq12345678"

driver = webdriver.Chrome(executable_path="E:\\c data\\Desktop\\operation63\\chromedriver.exe",chrome_options=options)
driver.get(url)
time.sleep(5)

#################################################################################
#googlesheets
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scopes=[
       'https://www.googleapis.com/auth/spreadsheets',
       'https://www.googleapis.com/auth/drive'
      ]

creds= ServiceAccountCredentials.from_json_keyfile_name("E:\\c data\\Desktop\\operation63\\googlesheets intergration python\\Dont CHANGE files\\operation63project.json", scopes=scopes)
file= gspread.authorize(creds)

workbook= file.open("operation63project")
sheet= workbook.sheet1

def log_in_first_time():
    Sumbit= driver.find_element(By.XPATH,"//*[contains(text(), 'Log in')]")
    Sumbit.click()
    time.sleep(5)

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

    #removing first  pop-ups sav-info
    if driver.find_element(By.CLASS_NAME,'_ac8f'):
        driver.find_element(By.CLASS_NAME,'_ac8f').click()
    time.sleep(10)

def send_mssg(sendto_id,sendto_mssg):
    #removing first  pop-ups sav-info
    try:
        driver.find_element(By.CLASS_NAME,'_ac8f').click()
    except NoSuchElementException:
        pass
    time.sleep(10)
    #click iwrite message icon
    driver.find_element(By.XPATH, "//div[contains(text(),'Send message')]").click()
    time.sleep(5)

    #enter client to name in search box
    driver.find_element(By.XPATH, "//input[@placeholder='Search...']").send_keys(sendto_id)
    time.sleep(5)
    #select client to in drop-down
    
    try:
        driver.find_element(By.XPATH,"//body//div//div[@role='dialog']//div[@role='dialog']//div//div//div//div[1]//div[1]//div[1]//div[1]//div[3]//div[1]//div[1]").click()
        driver.find_element(By.XPATH,"//div[contains(text(),'Chat')]").click()
        time.sleep(5)
    except NoSuchElementException:
        error_mssg="Make sure your friend is following snoopydoopy.official account"
    #Enter Message
    driver.find_element(By.XPATH,"//div[@aria-label='Message']").send_keys(sendto_mssg)
    driver.find_element(By.XPATH,"//div[normalize-space()='Send']").click()    
    
i=0
L=[]    
    
for j in range(i,100):
    if j in L:
        continue
    else:
        try:
            sendto_id=sheet.row_values(j)[1]
            sendto_mssg=sheet.row_values(j)[2]
            send_mssg(sendto_id,sendto_mssg)
            L.append(j)
            
        except IndexError:
            i=j
            break


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

    
