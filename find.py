from numpy import full_like
from var import FINAL_LINK, LAST, MAXIMIZE, CONTINUE

import pandas as pd
import json
from os import system, name

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

with open('data/jobs.json', 'r') as openfile:
    data_jobs = json.load(openfile)

try:
    jobs_arr_link = []
    for x in data_jobs:
        jobs_arr_link.append(x['link'])
except:
    pass

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


print("FINDING JOBS...")
clear()

def jobs_arr(link):

    driver.get(link)

    all_links = driver.find_elements(By.TAG_NAME, 'a')

    if len(all_links) <= 100:
        return False

    for i, job_link in enumerate(all_links):

        try:

            if "oferta-de-trabajo" in job_link.get_attribute("href"):

                try:
                    if job_link.get_attribute("href") in jobs_arr_link:
                        print('No new jobs founded')
                        return False

                except:
                    pass

                new_job = {
                    "name": job_link.text,
                    "link": job_link.get_attribute("href"),
                    "used": 0
                }

                data_jobs.append(new_job)

                # SAVE FILE
                with open("data/jobs.json", "w") as outfile:
                    json.dump(data_jobs, outfile)

        except:

            continue


for i in range(1, 30):

    link = f'{FINAL_LINK}{i}'

    print("job_qty: ", len(data_jobs))

    # print(already_saved_df.name)

    if jobs_arr(link) == False:

        break


driver.close()
