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
#W3_URL = 'https://www.w3schools.com/default.asp'



def W3Home(W3_URL):
    # Launch the browser
    global driver
    try:
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
        driver.implicitly_wait(12)
        driver.maximize_window()
        driver = driver
        driver.get(W3_URL)
        time.sleep(3)
        result=""
        if 'W3Schools Online Web Tutorials' in driver.title:
            #result="Login page reached"
            print("Login page reached")
            # Enter the AthenaUI Username and Password to login into Admin page
            time.sleep(1)
            result="Successfully navigated to W3"
            driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[3]/div[2]/div[2]').click()
            time.sleep(3)
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
#W3Home(W3_URL)


def HTMLNavigation():
    try:
        result=""
        global driver
        # Click the "Staging Page" button to enter into Staging interface
        driver.find_element_by_xpath('/html/body/nav[1]/div/a[1]').click()
        time.sleep(2)
        if 'HTML Tutorial' in driver.title:
            result="Successfully navigated to HTML page"
            #print(result)
            
        else:
            result="Unsuccessful, didn't reach HTML page"
            #print(result)
            
            
    except(NoSuchElementException, TimeoutException) as e:
        # fail the Test if the element can not be found or timeout occurs
        
        result="Test failed, HTML Navigation could not be found"
        print(result, e)
    time.sleep(3)
    return result
#HTMLNavigation()

def CSSNavigation():
    try:
        global driver
        # Click the "Kraken Page" button to enter into Staging interface
        result=""
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/a[4]').click()
        time.sleep(2)
        if "CSS Tutorial" in driver.title:
            result="Successfully navigated to CSS page"
            #print(result)
        else:
            result="Unsuccessful, didn't reach CSS page"
            #print(result)
            
    except(NoSuchElementException, TimeoutException) as e:
        # fail the Test if the element can not be found or timeout occurs
        result='Test failed, CSS Navigation could not be found '
        print(result, e)
        
    time.sleep(3)
    return result
#CSSNavigation()

def JavaScriptNavigation():
    
    try:
        global driver
        result=""
        # Click the "Maps Page" button to enter into Staging interface
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/a[5]').click()
        time.sleep(2)
        if "JavaScript Tutorial" in driver.title:
            result="Successfully navigated to JavaScript page"
            #print(result)
        else:
            result="Unsuccessful, didn't reach JavaScript page"
            #print(result)
    except(NoSuchElementException, TimeoutException) as e:
        # fail the Test if the element can not be found or timeout occurs
        result=" Test failed, JavaScript Navigation could not be found "
        print(result, e)
    time.sleep(3)
    return result
#JavaScriptNavigation()

def SQLNavigation():
    try:
        global driver
        result=""
        # Click the "Network Testing" button to enter into Network Testing interface
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/a[6]').click()
        time.sleep(2)
        if 'SQL Tutorial' in driver.title:
            result="Successfully navigated to SQL page"
        else:
            result="Unsuccessful, didn't reach SQL page"
            
    except(NoSuchElementException, TimeoutException) as e:
        # fail the Test if the element can not be found or timeout occurs
        result=" Test failed, SQL Navigation could not be found "
        print(result, e)
    time.sleep(3)
    return result
#SQLNavigation()



def PythonNavigation():
    try:
        global driver
        result=""
        # Click the "Network Testing" button to enter into Network Testing interface
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/a[7]').click()
        time.sleep(2)
        if 'Python Tutorial' in driver.title:
            result="Successfully navigated to Python page"
        else:
            result="Unsuccessful, didn't reach Python page"
            
    except(NoSuchElementException, TimeoutException) as e:
        # fail the Test if the element can not be found or timeout occurs
        result=" Test failed, Python Navigation could not be found "
        print(result, e)
    time.sleep(3)
    return result
#PythonNavigation()