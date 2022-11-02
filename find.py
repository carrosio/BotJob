from numpy import full_like
from var import FINAL_LINK, LAST, MAXIMIZE

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


job_list = []
already_saved_df = pd.read_json('data.json')


def jobs_arr(link):

    driver.get(link)

    all_links = driver.find_elements(By.TAG_NAME, 'a')

    print(len(all_links))

    if len(all_links) <= 100:
        return False

    for i, job_link in enumerate(all_links):

        try:

            if "oferta-de-trabajo" in job_link.get_attribute("href"):
                
                

                if job_link.text in already_saved_df.name.array:
                    print("Job already saved")
                    continue
                

                new_job = {
                    "name": job_link.text,
                    "link": job_link.get_attribute("href"),
                    "used": 0
                }

                job_list.append(new_job)
                
        except:

            continue




for i in range(1,30):
    
    link = f'{FINAL_LINK}{i}'

    print("job_qty: ", len(job_list))

    jobs_list_df = pd.DataFrame(job_list)

    if jobs_arr(link) == False:
        break

jobs_list_df.to_json('data.json')

driver.close()
