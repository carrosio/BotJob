
from var import FINAL_LINK, LAST, MAXIMIZE, POSTULATE

import pandas as pd
import json
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


if MAXIMIZE == 0:
    driver.minimize_window()
    print("Windows Minimized")
else:
    print("Windows Maximized")


df_Data = pd.read_json('data.json')

for i, job in enumerate(df_Data.link):
    driver.get(job)
    try:
        #CLICK on Postulate Link
        driver.find_element(By.XPATH, POSTULATE).click()
        df_Data.iloc[i].used = 1
        
    except:
        continue