"""
Selenium Webscraper for Agendamentos Online
Function enters personal details and looks for vacant passport booking.

Output is 1 if available, and 0 if not.
Chrome tab will be left open if appointment is available.
 
Created on Tue Jul 28 10:22:17 2022
Written by Jonathan De Sousa
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

    
def appointment_avail():
    pause = 1 #pause to slow down webscraping to help disguise bot.
    phrase_0 = 'There are no vacancies available right now'
    avail = 'FALSE'
    message = '---'
        
    c = webdriver.ChromeOptions()
    c.add_argument("--incognito")
    # c.add_argument("--start-maximized")
    
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    url = 'https://agendamentosonline.mne.gov.pt/AgendamentosOnline/index.jsf'

    driver = webdriver.Chrome(service=Service(PATH), options=c)
    driver.get(url)
    time.sleep(1)

    time.sleep(pause)
    
    # Accept cookies
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'j_idt68'))
        )
    element.click()
    
    time.sleep(pause)
    
    # Click Ok buttom of Information agreement
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'j_idt61'))
        )
    element.click()
    
    time.sleep(pause)
    
    # Change language from English to Portuguese
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'indexForm:langs'))
        )
    element.click()
    
    time.sleep(pause)
    
    lang = driver.find_element(by=By.XPATH, value="//div[@id='indexForm:langs_panel']/div[@class='ui-selectonemenu-items-wrapper']/ul[@class='ui-selectonemenu-items ui-selectonemenu-list ui-widget-content ui-widget ui-corner-all ui-helper-reset']/li[text()='English']")
    lang.click()
    
    time.sleep(pause)
    
    # Click Ok buttom of Information agreement (now in English)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'j_idt61'))
        )
    element.click()
    
    time.sleep(pause)
    
    # Click 'Schedule an appointment'
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'indexForm:j_idt29'))
        )
    element.click()
    
    time.sleep(pause)
    
    # Enter ID number
    ID = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'scheduleForm:tabViewId:ccnum'))
        )
    ID.clear()
    ID.send_keys('88888888') #enter ID number
    
    time.sleep(pause)
    
    # Enter date of birth
    DoB = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'scheduleForm:tabViewId:dataNascimento_input'))
        )
    DoB.clear()
    DoB.send_keys('01-01-1901') #enter date of birth
    DoB.send_keys(Keys.ESCAPE)
    
    time.sleep(pause)
    
    # Click 'Search'
    search = driver.find_element(by=By.ID, value='scheduleForm:tabViewId:searchIcon')
    search.click()
    
    time.sleep(pause)
    
    # Select consular post
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'scheduleForm:postcons_label'))
        )
    element.click()
    
    time.sleep(pause)
    
    post = driver.find_element(by=By.XPATH, value="//div[@id='scheduleForm:postcons_panel']/div[@class='ui-selectonemenu-items-wrapper']/ul[@class='ui-selectonemenu-items ui-selectonemenu-list ui-widget-content ui-widget ui-corner-all ui-helper-reset']/li[text()='General Consulate of Portugal in London']")
    post.click()
    
    time.sleep(pause)
    
    # Select consular act type
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'scheduleForm:categato_label'))
        )
    element.click()
    
    time.sleep(pause)
    
    actType = driver.find_element(by=By.XPATH, value="//div[@id='scheduleForm:categato_panel']/div[@class='ui-selectonemenu-items-wrapper']/ul[@class='ui-selectonemenu-items ui-selectonemenu-list ui-widget-content ui-widget ui-corner-all ui-helper-reset']/li[text()='Travel Documents']")
    actType.click()
    
    time.sleep(pause)
    
    # Select consular act
    time.sleep(0.75)
    element = WebDriverWait(driver, 10, ignored_exceptions=StaleElementReferenceException).until(
        EC.presence_of_element_located((By.ID, 'scheduleForm:atocons_label'))
        )
    element.click()
    
    time.sleep(pause)
    
    act = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='scheduleForm:atocons_panel']/div[@class='ui-selectonemenu-items-wrapper']/ul[@class='ui-selectonemenu-items ui-selectonemenu-list ui-widget-content ui-widget ui-corner-all ui-helper-reset']/li[text()='Portuguese Electronic Passport']"))
        )
    # act = driver.find_element(by=By.XPATH, value="//div[@id='scheduleForm:atocons_panel']/div[@class='ui-selectonemenu-items-wrapper']/ul[@class='ui-selectonemenu-items ui-selectonemenu-list ui-widget-content ui-widget ui-corner-all ui-helper-reset']/li[text()='Portuguese Electronic Passport']")
    act.click()
    
    time.sleep(pause)
    
    # Click 'Add consular act'
    time.sleep(0.5)
    element = WebDriverWait(driver, 10, ignored_exceptions=StaleElementReferenceException).until(
        EC.element_to_be_clickable((By.ID, 'scheduleForm:bAddAto'))
        )
    element.click()
    
    time.sleep(pause)
    
    # Accept terms and conditions
    time.sleep(0.5)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'scheduleForm:dataTableListaAtos:0:selCond'))
        )
    element.click()
    
    time.sleep(pause)
    
    # Schedule appointment
    time.sleep(0.5)
    element = WebDriverWait(driver, 10, ignored_exceptions=StaleElementReferenceException).until(
        EC.presence_of_element_located((By.ID, 'scheduleForm:dataTableListaAtos:0:bCal'))
        )
    element.click()
    
    # time.sleep(2) #debugging purpose
    
    # CAPTCHA pops up here occassionally, but if no vacancy exists the same 
    # HTML element displaying the appointment info is present but is hidden 
    # by the CAPTCHA element. 
    # Hence, still check for the no vacancy message regardless of CAPTCHA 
    # presence.
    
    try:
        # Read appointment information
        info = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='scheduleForm:j_idt171']/div[@class='ui-dialog-content ui-widget-content']/table[@style='font-size: 12pt; padding-top: 2%; text-align: center; vertical-align: middle; margin:0 auto;']/tbody/tr/td"))
            )
        
        
        time.sleep(1)
        message = info.text
        print('Info message: ', message) # debugging purposes
        
        #time.sleep(0.5) #pause needed to read text from info
        if not phrase_0 in message:
            avail = 'TRUE'
        else:
            time.sleep(1.5) #debugging purposes -- remove when code is finalised
            driver.close()
        
    except:
        avail = 'TRUE'

    # driver has to be returned else tab closes even if driver.close() is not 
    # used
    return avail, driver, message