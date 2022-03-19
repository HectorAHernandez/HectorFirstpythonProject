# To automate an UI application the fist thing is to invoke the browser that we will be
# using to handle the UI, for this in Python we import the Selenium webdriver class package, so type
# webdriver and when the system ask to import it select "Selenium.webdriver":
import time

from selenium import webdriver

# this webdriver package contains all the different browsers (Edge,edge,Firefox,firefox,
# Chrome, chrome... we have to select the ones starting in Uppercase)
# Now create the object to instantiate the class of the browser select from the webdriver

# hhDriver01 = webdriver.Chrome(executable_path=xxxx)
# driver02 = webdriver.Edge(executable_path=xxxx)
# hdriver03 = webdriver.Firefox(executable_path=xxxx)
# driver = webdriver.Safari(executable_path=xxxx)

# 1- Each browser exposes an executable file/program to allow Selenium automation to run commands
# this is, in automation, for selenium to be able to invoke an specific browser, it needs to use the
# specific browser executable file/program.
# 2- Through Python-Selenium code we need to invoke this executable file/program which then
# will invoke he actual browser, so in the webdriver.Chrome(executable_path=c:\\fileloc) we have to
# provision the path where we have downloaded this executable file in our local/server file system, _path:
# this is :

#hhDriver01 = webdriver.Chrome(executable_path="C:\\Selenium\\BrowserExecutableFiles\\chromedriver.exe")
#driver02 = webdriver.Edge(executable_path="C:\\Selenium\\BrowserExecutableFiles\\msedgedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\Selenium\\BrowserExecutableFiles\\geckodriver.exe")
#hdriver03 = webdriver.Opera(executable_path="C:\\Selenium\\BrowserExecutableFiles\\operadriver.exe")

# the above instantiated driver object can now be used to access all the methods needed to
# get information from the the browser and to send and retrieve data to/from the browser.
# for example if we want to open (driver.get(url) the website www.rahulshettyacademy.com we can use:
# with Chrome:
#hhDriver01.get("https://www.rahulshettyacademy.com")  # get() opens the indicated url
# with Edge browser:
#driver02.get("https://www.rahulshettyacademy.com")   # driver.get() opens the url
# with Firefox browser:
pageUrl = "https://www.rahulshettyacademy.com"
driver.get(pageUrl)  # driver.get() opens the url
driver.maximize_window()  # To Maximize the windows when the browse is opened with .get(url)
# with Opera browser:
# hdriver03.get("https://www.rahulshettyacademy.com")  # the object driver.get() opens the url

# From now on all command will be using the Firefox broswer with the object-driver = driver
# to get the title of the current open page, use the method object-driver.title command
pageTitle = driver.title
print("page title:",pageTitle)

# to get the current page url or the url of the landed paged, use the method object-driver.current_url
# this information can be used in an assertion to determine if the webpage has been hacked, by
# comparing if the current_url is different than the one we used in the get(url) to open the page.
landedUrl = driver.current_url
print("pageUrl: ", pageUrl)
print("LandedUrl: ", landedUrl)
# assert (pageUrl == landedUrl)

time.sleep(2) # make Python to halt executin for 2 seconds.
practiceWebsite = "https://www.rahulshettyacademy.com/#/practice-project"
driver.get(practiceWebsite)
driver.minimize_window()  # To minimize the windows when the browse is opened with .get(url)
# order statements with the practiceWebsit
#time.sleep(3)  # make Python to halt executin for 3 seconds.
driver.back()  # click on the back button to get back to the previous page.
driver.refresh()  # refresh the returned page after clicking the Back button.

#driver.close()  # close the current windows that were open with the driver.get() method.
                # if we have just opened a child window, only the child window will be closed.
#driver.quit()   # close all the windows that have been opened by the automation program.
                # if we have just opened a child window, with .quit() method both/all windows
                #  will be closed.

