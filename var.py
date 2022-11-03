# CONFIG

#['ar', 'uy']
COUNTRY = 'ar'

if COUNTRY == 'uy':
    ZONE = 'montevideo'
if COUNTRY == 'ar':
    ZONE = 'capital-federal'


#TIME = ['recent', '1d', '7d']

LAST = 30

MAXIMIZE = 1

FINAL_LINK = f'https://{COUNTRY}.computrabajo.com/empleos-en-{ZONE}?by=publicationtime&pubdate=1&p='

# XPATH

POSTULATE = "/html/body/main/div[2]/div/div[2]/div[2]/div[2]/div/a"

LOGGIN_TEXT = '/html/body/section/div/form/div[1]/p[3]'

CONTINUE = True
