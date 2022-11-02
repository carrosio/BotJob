
from var import FINAL_LINK, LAST, MAXIMIZE, POSTULATE, LOGGIN_TEXT

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

#print("Current session is {}".format(driver.session_id))


def loggin():
    try:
        #driver.find_element(By.ID, POSTULATE)
        mail_btm = driver.find_element(
            By.XPATH, '/html/body/section/div/form/div[1]/div[3]/input')
        mail_btm.send_keys("carrosiomauricio@gmail.com")
        continue_btm = driver.find_element(
            By.XPATH, "/html/body/section/div/form/div[1]/a")
        continue_btm.click()
        time.sleep(9999)

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


if MAXIMIZE == 0:
    driver.minimize_window()
    print("Windows Minimized")
else:
    print("Windows Maximized")


df_Data = pd.read_json('data.json')

for i, job in enumerate(df_Data.link):
    # print(job)
    if df_Data.loc[i, 'used'] == 1:
        print("Job already used, skiped.", i)
        continue

    driver.get(job)
    try:
        # CLICK on Postulate Link
        driver.find_element(By.XPATH, POSTULATE).click()
        df_Data.loc[i, 'used'] = 1
        print("Job Postultaed!", i)
        loggin()
        df_Data.to_json('data.json')

    except:
        continue
