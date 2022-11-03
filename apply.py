
from var import FINAL_LINK, MAXIMIZE, COUNTRY, POSTULATE, LOGGIN_TEXT, CONTINUE


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

if CONTINUE:
        
    if MAXIMIZE == 0:
        driver.minimize_window()
        print("Windows Minimized")
    else:
        print("Windows Maximized")


    with open('data/jobs.json', 'r') as openfile:
        data_jobs = json.load(openfile)


    print("POSTULATING TO JOBS...")
    #clear()

    for i, job in enumerate(data_jobs):

        all_p = driver.find_elements(By.TAG_NAME, 'p')

        if job['used'] == 1:
            print('job already taken!', job['name'])
            continue

        else:

            driver.get(job['link'])

            try:
            # CLICK on Postulate Link
                driver.find_element(By.XPATH, POSTULATE).click()
                #try:
                #    driver.find_element(By.XPATH, '/html/body/div/form/div/article/div[1]/div[2]/p[1]')
                #    job['used'] = 2
                #except:
                #    pass

                job['used'] = 1
                
                print("#", len(data_jobs) - i , "Job Postultaed!", job['name'])

                loggin()
            # SAVE FILE
                with open("data/jobs.json", "w") as outfile:
                    json.dump(data_jobs, outfile)

            except:
                continue

else:
    print("Processs ended until no new job to apply!")
    
driver.close()