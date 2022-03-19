from selenium import webdriver
# this program introduce the use of Chrome browser Options.
# In the definition of the driver object, so far, we have only use the 'executable_path=' option,
# but now we are going to expand to use other Chrome browser options on how to invoke the browser
# at execution time. to do this we will use the 'chromeOptions' class so that we can create an object to
# define how we want he browser to behave at execution time.

chrome_optionsObject = webdriver.ChromeOptions()
chrome_optionsObject.add_argument("--start-maximized")  # to start the browser in maximized mode.

chrome_optionsObject.add_argument("headless")
# headless: run the program in the background, this is the webpage operation won't be seen while
# execution. only the end result will be indicated in the console. This headless option is very
# useful because the execution run faster (no Input/Output is generated to the screen) and uses
# less memory from the RAM

chrome_optionsObject.add_argument("--ignore-certificate-errors")
# this ignore the request for certification in certain webPage we use the xxxx browser option, this
# avoid the SSS Certification Error generation when trying to access the page. This option will,
# automatically, made the browser to click Accept and continue with the login process and ignore any
# certificate error and continue to the webpage.

# *** This website provides example of multiple Chrome options that we can use:
#     https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

# now we have to append this chrome_optionsObject object to the webDriver invoke statement after
# the 'executable_path=' argument:

driver = webdriver.Chrome(executable_path="C:\\Selenium\\BrowserExecutableFiles\\chromedriver.exe",
                          options=chrome_optionsObject)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print("The title of the page is: ", driver.title)