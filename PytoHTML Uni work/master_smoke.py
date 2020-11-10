#imports all librarys
import time
import Navigation_YouTube
import Navigation_Twitter
import Navigation_W3Schools
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import requests
import urllib
import PytoHTML
import PytoHTML_failed
from selenium import webdriver
import selenium
import slack
import os

W3_URL = 'https://www.w3schools.com/default.asp'
Twitter_URL = 'https://twitter.com/explore'
YT_URL = 'https://www.youtube.com/'
celeb = '@realDonaldTrump'

###  If you want failed script to run, change between 1 and 2  ###

###  1 - Pass - Unhash line 27 and hash line 30 for W3 to Pass ###
PassOrFail = 'Python Tutorial'

###  2 - Fail - Unhash line 30 and hash line 27 for W3 to Fail ###
#PassOrFail = 'W3 table will fail'



#proxy = {
#    "http": "proxy.room101.com:8080",
#    "https": "proxy.room101.com:8080"
#             }

#every result needs to be recorded so can be added to a DB


def main():
    #call of the tests here
        global YouTube
        global Twitter
        global W3
        global driver
        YouTube = YouTube()
        Twitter = Twitter()
        W3 = W3()
        
        table = Table_Creation()
        

        message = (str(YouTube) + "\n \n" + str(Twitter) + "\n \n" + str(W3))
        time.sleep(1)
        #will send a message
        dataRequest = {'test_results': message}
        #C:\PnB_Selenium_Scripts\Master Smoke\ScreenShots\SmokeFailed.png
#### Creates table for failed only to post to slack ####
        #Table_Failed()
        table = PytoHTML_failed
        time.sleep(2)
        table.Table_Start()
        if ("Failed" in YouTube):
            print("YouTube failed")
            table.Table_html("YouTubeResults.txt", "YouTube - Failed")
        else:
            print("YouTube passed")
            
        if ("Failed" in Twitter):
            print("Twitter failed")
            table.Table_html("TwitterResults.txt", "Twitter - Failed")
        else:
            print("Twitter passed")
            
        if ("Failed" in W3):
            print("W3 failed")
            table.Table_html("W3Results.txt", "W3 - Failed")
        else:
            print("W3 passed")
            
####Takes a screenshot of the html tables####
        take_screenshot()
        time.sleep(2)
####fail build if any test has failed####
        if("Failed" in message):
            failed_slack()
            time.sleep(2)
            print("It failed")
            emails(message, "failed")
            sys.exit(-1)
        else:
            emails(message, "pass")





def emails(messageToSend, result):
    server = smtplib.SMTP('smtp.room101.com')
    to_email = ["jack.wynn@bt.com"]
    from_email = 'jack.wynn@bt.com'
    
    subject = 'Kraken Smoke Test Results'

    if(result=="pass"):
        subject = 'Kraken Smoke Test Result - PASS'
    else:
        subject = 'Kraken Smoke Test Results - FAIL'
    
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = from_email
    message['To'] = ", ".join(to_email)

    # Send the mail
    f=open(r"C:\Users\612686463\OneDrive - BT Plc\Documents\Apprenticeship\University\Year 1\Term2\Software\Assignment\PytoHTML Uni work\ScreenShots\SmokeFailed.png", "r")
    html=f.read()
    message.attach(MIMEText(html, "html"))
    msgBody = message.as_string()
    server.sendmail(from_email, to_email, msgBody)
    server.quit()







def YouTube():
        global driver
        try:
                #this will be where we assert each test for YouTube
                results="Steps: Results \n"
                
                
                
                #login to athena_UI
                login= Navigation_YouTube.YouTubeHome(YT_URL)
                
                if ("Successfully navigated to YouTube" == login):
                    #this is where should write the result to DB longer term
                    print("Login: Pass")
                    results = results+"Login: Pass \n"
                else:
                    print ("Login: Failed")
                    results = results + "Login: Failed \n"



                #run selenium for staging navigation
                TrendingNav= Navigation_YouTube.TrendingNavigation()
                
                if("Successfully navigated to Trending page" == TrendingNav):
                    print("Trending: Pass")
                    results = results + "Trending: Pass \n"
                else:
                    print ("Trending: Failed")
                    results = results + "Trending: Failed \n"



                #run selenium for recon navigation
                SubscriptionsNav= Navigation_YouTube.SubscriptionsNavigation()
                
                if("Successfully navigated to Subscriptions page" == SubscriptionsNav):
                    print("Subscriptions: Pass")
                    results = results + "Subscriptions: Pass \n"
                else:
                    print("Subscriptions: Failed")
                    results = results + "Subscriptions: Failed \n"




                #run selenium for config navigation
                LibraryNav= Navigation_YouTube.LibraryNavigation()

                if("Successfully navigated to Library page" == LibraryNav):
                    print("Library: Pass")
                    results = results + "Library: Pass \n"
                else:
                    print("Library: Failed")
                    results = results + "Library: Failed \n"



                #run selenium for network tests navigation
                HistoryNav= Navigation_YouTube.HistoryNavigation()
                
                if("Successfully navigated to History page" == HistoryNav):
                    print("History: Pass")
                    results = results + "History: Pass \n"
                else:
                    print("History: Failed")
                    results = results + "History: Failed \n"



        finally:
                #Navigation_YouTube.driver.close()
                #Navigation_YouTube.driver.quit()
                f = open("YouTubeResults.txt", "w")
                f.write(results)
                f.close()
        return results
    
    
    
    
    
def Twitter():
        global driver
        try:
                #this will be where we assert each test for YouTube
                results="Steps: Results \n"
                
                
                
                #login to athena_UI
                login= Navigation_Twitter.TwitterHome(Twitter_URL)
                
                if ("Successfully navigated to Twitter" == login):
                    #this is where should write the result to DB longer term
                    print("Login: Pass")
                    results = results+"Login: Pass \n"
                else:
                    print ("Login: Failed")
                    results = results + "Login: Failed \n"



                #run selenium for staging navigation
                CelebNav= Navigation_Twitter.CelebNavigation()
                
                if("Successfully navigated to Celeb page" == CelebNav):
                    print("Celeb: Pass")
                    results = results + "Celeb: Pass \n"
                else:
                    print ("Celeb: Failed")
                    results = results + "Celeb: Failed \n"



                #run selenium for recon navigation
                TRNav= Navigation_Twitter.TRNavigation()
                
                if("Successfully navigated to TR page" == TRNav):
                    print("TR: Pass")
                    results = results + "TR: Pass \n"
                else:
                    print("TR: Failed")
                    results = results + "TR: Failed \n"



        finally:
                #Navigation_YouTube.driver.close()
                #Navigation_YouTube.driver.quit()
                f = open("TwitterResults.txt", "w")
                f.write(results)
                f.close()
        return results





def W3():
        global driver
        try:
                #this will be where we assert each test for YouTube
                results="Steps: Results \n"
                
                
                
                #login to athena_UI
                login= Navigation_W3Schools.W3Home(W3_URL)
                
                if ("Successfully navigated to W3" == login):
                    #this is where should write the result to DB longer term
                    print("Login: Pass")
                    results = results+"Login: Pass \n"
                else:
                    print ("Login: Failed")
                    results = results + "Login: Failed \n"



                #run selenium for staging navigation
                HTMLNav= Navigation_W3Schools.HTMLNavigation()
                
                if("Successfully navigated to HTML page" == HTMLNav):
                    print("HTML: Pass")
                    results = results + "HTML: Pass \n"
                else:
                    print ("HTML: Failed")
                    results = results + "HTML: Failed \n"



                #run selenium for recon navigation
                CSSNav= Navigation_W3Schools.CSSNavigation()
                
                if("Successfully navigated to CSS page" == CSSNav):
                    print("CSS: Pass")
                    results = results + "CSS: Pass \n"
                else:
                    print("CSS: Failed")
                    results = results + "CSS: Failed \n"




                #run selenium for config navigation
                JavaScriptNav= Navigation_W3Schools.JavaScriptNavigation()

                if("Successfully navigated to JavaScript page" == JavaScriptNav):
                    print("JavaScript: Pass")
                    results = results + "JavaScript: Pass \n"
                else:
                    print("JavaScript: Failed")
                    results = results + "JavaScript: Failed \n"



                #run selenium for network tests navigation
                SQLNav= Navigation_W3Schools.SQLNavigation()
                
                if("Successfully navigated to SQL page" == SQLNav):
                    print("SQL: Pass")
                    results = results + "SQL: Pass \n"
                else:
                    print("SQL: Failed")
                    results = results + "SQL: Failed \n"
                    
                    
                    
                #run selenium for Python navigation
                PythonNav= Navigation_W3Schools.PythonNavigation(PassOrFail)
                
                if("Successfully navigated to Python page" == PythonNav):
                    print("Python: Pass")
                    results = results + "Python: Pass \n"
                else:
                    print("Python: Failed")
                    results = results + "Python: Failed \n"    



        finally:
                #Navigation_YouTube.driver.close()
                #Navigation_YouTube.driver.quit()
                f = open("W3Results.txt", "w")
                f.write(results)
                f.close()
        return results



def Table_Creation():
        
        table = PytoHTML
        table.Table_Start()        
        table.Table_html("TwitterResults.txt", "Twitter")
        table.Table_html("W3Results.txt", "W3")
        table.Table_html("YouTubeResults.txt", "YouTube")



def Table_Failed():
    global Twitter
    global YouTube
    global W3

    table = PytoHTML_failed
    table.Table_Start()
    if ("Failed" in YouTube):
        print("YouTube failed")
        table.Table_html("YouTubeResults.txt", "YouTube Failed")
    else:
        print("YouTube passed")
        
            
    if ("Failed" in Twitter):
        print("Twitter failed")
        table.Table_html("TwitterResults.txt", "Twitter Failed")
    else:
        print("Twitter passed")
            
        
    if ("Failed" in W3):
        print("W3 failed")
        table.Table_html("W3Results.txt", "W3 Failed")
    else:
        print("W3 passed")



def take_screenshot():
    CHROMEDRIVER_PATH = r'C:\Users\612686463\OneDrive - BT Plc\Documents\Apprenticeship\University\Year 1\Term2\Software\Assignment\PytoHTML Uni work\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
    driver.maximize_window()
    driver.get(r"C:\Users\612686463\OneDrive - BT Plc\Documents\Apprenticeship\University\Year 1\Term2\Software\Assignment\PytoHTML Uni work\SmokeFailed.html")
    driver.save_screenshot(r"C:\Users\612686463\OneDrive - BT Plc\Documents\Apprenticeship\University\Year 1\Term2\Software\Assignment\PytoHTML Uni work\ScreenShots\SmokeFailed.png")
    driver.quit()




def failed_slack():
    slack_token = ('xoxb-1458606813366-1458697740822-yxD8jgbLkQ0sOeQJnNqHvWNU')
    client = slack.WebClient(token=slack_token, proxy=proxy)
    response = client.files_upload(    
        file=r'C:\Users\612686463\OneDrive - BT Plc\Documents\Apprenticeship\University\Year 1\Term2\Software\Assignment\PytoHTML Uni work\ScreenShots\SmokeFailed.png',
        initial_comment='Smoke Failed Results',
        channels='#2-failed-results-channel'

    )




main()
