#import ctypes
#from datetime import date, timedelta
#import datetime
#import sys
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
#YT_URL = 'https://www.youtube.com/'



def YouTubeHome(YT_URL):
    # Launch the browser
    global driver
    try:
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
        driver.implicitly_wait(12)
        driver.maximize_window()
        driver = driver
        driver.get('https://www.youtube.com/')#YT_URL)
        time.sleep(3)
        result=""
        if 'YouTube' in driver.title:
            #result="Login page reached"
            print("Login page reached")
            # Enter the AthenaUI Username and Password to login into Admin page
            time.sleep(1)
            result="Successfully navigated to YouTube"
            driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/paper-button/yt-formatted-string').click()
            time.sleep(1)
            print('USER - (If google cookie menu pops up) - Please click on "I agree" - (Else ignore)')
            time.sleep(15)
            print("Thank you")
            time.sleep(2)
        else:
            result= "Page not reached successfully"
            print (result)
    except NoSuchElementException as e:
        print(result, e)

    return result
#youtubehome(YT_URL)


def TrendingNavigation():
    try:
        result=""
        global driver
        # Click the "Staging Page" button to enter into Staging interface
        driver.find_element_by_xpath('/html/body/ytd-app/div/app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[2]/a/paper-item/yt-formatted-string').click()
        time.sleep(2)
        if 'Trending - YouTube' in driver.title:
            result="Successfully navigated to Trending page"
            #print(result)
            
        else:
            result="Unsuccessful, didn't reach Trending page"
            #print(result)
            
            
    except(NoSuchElementException, TimeoutException) as e:
        # fail the Test if the element can not be found or timeout occurs
        
        result="Test failed, Trending Navigation could not be found"
        print(result, e)
    time.sleep(3)
    return result
#TrendingNavigation()

def SubscriptionsNavigation():
    try:
        global driver
        # Click the "Kraken Page" button to enter into Staging interface
        result=""
        driver.find_element_by_xpath('/html/body/ytd-app/div/app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[3]/a/paper-item/yt-formatted-string').click()
        time.sleep(2)
        if "Subscriptions - YouTube" in driver.title:
            result="Successfully navigated to Subscriptions page"
            #print(result)
        else:
            result="Unsuccessful, didn't reach Subscriptions page"
            #print(result)
            
    except(NoSuchElementException, TimeoutException) as e:
        # fail the Test if the element can not be found or timeout occurs
        result='Test failed, Subscriptions Navigation could not be found '
        print(result, e)
        
    time.sleep(3)
    return result
#SubscriptionsNavigation()

def LibraryNavigation():
    
    try:
        global driver
        result=""
        # Click the "Maps Page" button to enter into Staging interface
        driver.find_element_by_xpath('/html/body/ytd-app/div/app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[2]/div/ytd-guide-entry-renderer[1]/a/paper-item/yt-formatted-string').click()
        time.sleep(2)
        if "Library - YouTube" in driver.title:
            result="Successfully navigated to Library page"
            #print(result)
        else:
            result="Unsuccessful, didn't reach Library page"
            #print(result)
    except(NoSuchElementException, TimeoutException) as e:
        # fail the Test if the element can not be found or timeout occurs
        result=" Test failed, Library Navigation could not be found "
        print(result, e)
    time.sleep(3)
    return result
#LibraryNavigation()

def HistoryNavigation():
    try:
        global driver
        result=""
        # Click the "Network Testing" button to enter into Network Testing interface
        driver.find_element_by_xpath('/html/body/ytd-app/div/app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[2]/div/ytd-guide-entry-renderer[2]/a/paper-item/yt-formatted-string').click()
        time.sleep(2)
        if 'YouTube' in driver.title and 'history' not in driver.title:
            result="Successfully navigated to History page"
        else:
            result="Unsuccessful, didn't reach History page"
            
    except(NoSuchElementException, TimeoutException) as e:
        # fail the Test if the element can not be found or timeout occurs
        result=" Test failed, History Navigation could not be found "
        print(result, e)
    time.sleep(3)
    return result
    driver.close()
    driver.quit()
#HistoryNavigation()



