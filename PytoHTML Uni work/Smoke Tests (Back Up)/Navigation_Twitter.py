import ctypes
from datetime import date, timedelta
import datetime
import sys
import time
from selenium import webdriver
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


CHROMEDRIVER_PATH = r'C:\Users\612686463\OneDrive - BT Plc\Documents\Apprenticeship\University\Year 1\Term2\Software\Assignment\PytoHTML Uni work\chromedriver.exe'
Twitter_URL = 'https://twitter.com/explore'
celeb = "@realDonaldTrump"


def TwitterHome(Twitter_URL):
    # Launch the browser
    global driver
    try:
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
        driver.implicitly_wait(12)
        driver.maximize_window()
        driver = driver
        driver.get(Twitter_URL)
        time.sleep(3)
        result=""
        if 'Explore / Twitter' in driver.title:
            #result="Login page reached"
            print("Login page reached")
            # Enter the AthenaUI Username and Password to login into Admin page
            time.sleep(1)
            result="Successfully navigated to Twitter"
            print('USER - (If google cookie menu pops up) - Please click on "I agree" - (Else ignore)')
            time.sleep(10)
            print("Thank you")
            time.sleep(2)
        else:
            result= "Page not reached successfully"
            print (result)
    except NoSuchElementException as e:
        print(result, e)

    return result
#TwitterHome(Twitter_URL)


def CelebNavigation():
    try:
        result=""
        global driver
        # Click the "Staging Page" button to enter into Staging interface
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input').send_keys(celeb)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div/div[6]/div/li/div/div[2]/div/div/div/div[2]/div/span').click()
        time.sleep(2)
        if 'Donald J. Trump' in driver.title:
            result="Successfully navigated to Celeb page"     
        else:
            result="Unsuccessful, didn't reach Celeb page"
            #print(result)
            
    except(NoSuchElementException, TimeoutException) as e:
        # fail the Test if the element can not be found or timeout occurs
        
        result="Test failed, Celeb Navigation could not be found"
        print(result, e)
    time.sleep(3)
    return result
#CelebNavigation()

def TRNavigation():
    try:
        global driver
        # Click the "Kraken Page" button to enter into Staging interface
        result=""
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/nav/div/div[2]/div/div[2]/a/div/span').click()
        time.sleep(2)
        if "Tweets with replies6" in driver.title:
            result="Successfully navigated to TR page"
            #print(result)
        else:
            result="Unsuccessful, didn't reach TR page"
            #print(result)
            
    except(NoSuchElementException, TimeoutException) as e:
        # fail the Test if the element can not be found or timeout occurs
        result='Test failed, TR Navigation could not be found '
        print(result, e)
        
    time.sleep(3)
    return result
#TRNavigation()



