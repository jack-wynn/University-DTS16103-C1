# University-DTS16103-C1 - Jack Wynn


INTRODUCTION
------------

 

This is a collection of Python scripts including Python Selenium scripts that use a rangeof code to navigate websites and test whether the navigation is working.  I am then collecting this data and visualising it within a HTML table, which will display the results in a neat and professional format, plus send this table via email and/or Slack depending on the results.

 

REQUIREMENTS
------------

 

For the scripts to work, the following libraries are required;



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

 

HOW TO USE
-----------

 

It is quite a complicated set of scripts to get your head around, but as long as you just stick to the main script "master_smoke", you should be fine.  You need to open master_smoke, which will have all the other scripts functions called within it.  You can change line 27 and 30 to be commented/uncommented, which will switch it between all passed results or a failed one within the W3 table. 

 

FURTHER IMPROVEMENTS
-----------

 



 

REFERENCES
-----------

 


