"""
Selenium Webscraper for Agendamentos Online
Script looks for vacant passport booking and sends SMS to phone if vacancy exists.

Created on Sat Jul 25 10:58:24 2022
Written by Jonathan De Sousa
"""

from appointment_avail_func import appointment_avail
from send_SMS_func import send_SMS
import time

#%%
pause_time = 2*60 #pause (in seconds) between vacancy checks
avail = 'FALSE' #availability

#%% Look for vacancy to become available

count = 1 #---------------------------------------debugging purposes

while avail == 'FALSE':
    avail, driver, info = appointment_avail()
    
    if avail == 'TRUE':
        break
    time.sleep(pause_time)
    
    count += 1 #----------------------------------debugging purposes
    #if count == 100: #----------------------------debugging purposes
    #    break

#%% Send SMS to cellphone when vacancy becomes available

destination = '+441759621104'
message = 'Vacancy available!'

send_SMS(destination, message)
