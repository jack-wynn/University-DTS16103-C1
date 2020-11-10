# University-DTS16103-C1 - Jack Wynn


INTRODUCTION
------------

 

This is a collection of Python scripts including Python Selenium scripts that use a rangeof code to navigate websites and test whether the navigation is working.  I am then collecting this data and visualising it within a HTML table, which will display the results in a neat and professional format, plus send this table via email and/or Slack depending on the results.

 

REQUIREMENTS
------------

 

For the scripts to work, the following libraries are required;



For the following script to work you will need to install these required libraries;

 
-	time
-	smtplib
-	email.mime.text
-	email.mime.multipart
-	sys
-	requests
-	os

 

All of these libraries are included as part of the standard python 3.9.0 libraries.

 

You will also need to pip install the following libraries

 


	
- urllib https://docs.python.org/3/library/urllib.html
- selenium https://seleniumpython.readthedocs.io/
- slack https://api.slack.com/tools
 

HOW TO USE
-----------

 

It is quite a complicated set of scripts to get your head around, but as long as you just stick to the main script "master_smoke", you should be fine.  You need to open master_smoke, which will have all the other scripts functions called within it.  You can change line 27 and 30 to be commented/uncommented, which will switch it between all passed results or a failed one within the W3 table. This way you can see the Failed_HTML table aswell.

 


REFERENCES
-----------

 

- PyPI. 2020. Selenium. [online] Available at: <https://pypi.org/project/selenium/> [Accessed 10 November 2020].

- Selenium-python.readthedocs.io. 2020. 7. Webdriver API — Selenium Python Bindings 2 Documentation. [online] Available at: <https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.keys> [Accessed 10 November 2020].

- Slack. 2020. Tutorials About "Python". [online] Available at: <https://api.slack.com/tutorials/tags/python> [Accessed 10 November 2020].

