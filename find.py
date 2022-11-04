from numpy import full_like
from var import FINAL_LINK, MAXIMIZE, CONTINUE

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

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()

if MAXIMIZE == 0:
    driver.minimize_window()
    print("Windows Minimized")
else:
    print("Windows Maximized")

with open('data/jobs.json', 'r') as openfile:
    data_jobs = json.load(openfile)


jobs_arr_link = []

try:

    for x in data_jobs:
        jobs_arr_link.append(x['name'])

except:

    pass



def jobs_arr(link):

    driver.get(link)

    all_links = driver.find_elements(By.TAG_NAME, 'a')

    for i, job_link in enumerate(all_links):

        try:

            #check the JOBS LINKS
            if "oferta-de-trabajo" in job_link.get_attribute("href"):
                
                if job_link.text in jobs_arr_link:
                    
                    print('Job Already saved')
                    
                    return False

                print("New Job Added!", job_link.text)
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


temp_apply_jobs = []
prev_data_jobs_len = len(data_jobs)

for i in range(1, 5):

    link = f'{FINAL_LINK}{i}'

    if jobs_arr(link) == False:
        print("New Jobs Finded: ", len(data_jobs) - prev_data_jobs_len)
        break

    print("Next Page")
    print("Already Saved Jobs Qty: ", len(data_jobs))
    

driver.close()
