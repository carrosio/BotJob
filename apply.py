
from var import FINAL_LINK, MAXIMIZE, COUNTRY, POSTULATE, LOGGIN_TEXT, CONTINUE
from os import system, name

import pandas as pd
import json
import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By


# Selenium Conections
chromeDriverPath = '/home/mauri/Documents'
profilePath = '/home/mauri/.config/google-chrome-beta/'
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument(f"--user-data-dir={profilePath}")
driver = webdriver.Chrome(options=chromeOptions)
driver.set_window_size(600, 1000)

postulated = 0

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()

def loggin():
    try:
        #driver.find_element(By.ID, POSTULATE)
        mail_btm = driver.find_element(
            By.XPATH, '/html/body/section/div/form/div[1]/div[3]/input')
        
        mail = "carrosiomauricio@gmail.com"
        if COUNTRY == 'ar':
            mail = "pepemauri25@gmail.com"
        mail_btm.send_keys(mail)

        continue_btm = driver.find_element(
            By.XPATH, "/html/body/section/div/form/div[1]/a")
        continue_btm.click()
        time.sleep(2)

        password_btm = driver.find_element(
            By.XPATH, "/html/body/section/div/form/div[2]/input")
        password_btm.send_keys("Loco8Molina")
        next_btm = driver.find_element(
            By.XPATH, "/html/body/section/div/form/div[2]/button")
        next_btm.click()
        pass

        """driver.get(job)
        driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[2]/div[2]/div[2]/div/a").click()"""
    except:

        pass

with open('used.json', 'r') as openfile:
    used_jobs = json.load(openfile)

data_jobs = pd.read_json('data.json')

jobs_links_arr = data_jobs.id.array
#print(data_jobs)
for i, job in enumerate(jobs_links_arr):

    proceded = round((i / len(jobs_links_arr))* 100) 

    print("Proceded Jobs: ", proceded, "%")

    if job in used_jobs:
        print("Already used", job)
        continue
    
    link = f'https://ar.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-{job}#lc=ListOffers-Score-0'
    
    driver.get(link)

    try:
        driver.find_element(By.XPATH, POSTULATE).click()
        print("Posutlated!", job)

        used_jobs.append(job)
        
        with open("used.json", "w") as outfile:
                    json.dump(used_jobs, outfile)

        

    except:
        continue
    

driver.close()