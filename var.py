#CONFIG

COUNTRY = ['ar', 'uy']
TIME = ['recent', '1d', '7d']
ZONE = ['capital-federal', 'montevideo']
LAST = 30
MAXIMIZE = 1

FINAL_LINK = f'https://{COUNTRY[1]}.computrabajo.com/empleos-en-{ZONE[1]}?by=publicationtime&pubdate=1&p='

#XPATH

POSTULATE = "/html/body/main/div[2]/div/div[2]/div[2]/div[2]/div/a"

LOGGIN_TEXT = '/html/body/section/div/form/div[1]/p[3]'