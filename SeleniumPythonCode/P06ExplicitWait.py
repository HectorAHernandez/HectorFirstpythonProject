# This program show how to use the Explicit Wait. This is useful when we
# have an application that needs to wait for a response before the program continue execution of
# a webDriver statement,
# i.e. A Product sale application that at the shopping cart level, when clicking for applying
# a discount the application has to wait to see if the discount was successfully approved.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Selenium\\BrowserExecutableFiles\\chromedriver.exe")

# EXPLICIT wait is used to target execution of specific webdriver command/statement, and
#  indicates that, before starting execution of the target webDriver statement, wait for 5 (x) seconds
#  for the specified webElement/object to become available. This waiting time is for giving time for
#  the specific webElement required for the execution (that normally are
# created by the execution of previous webDriver statements) to become available and
# avoid that the program fail with error:
#     raise exception_class(message, screen, stacktrace)
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable
#                to locate element: {"method":"css selector","selector":".promoCode"}
#   (Session info: chrome=93.0.4577.63)
# OR THIS OTHER ERROR:
#    raise exception_class(message, screen, stacktrace)
# selenium.common.exceptions.StaleElementReferenceException: Message: stale element
#                reference: element is not attached to the page document
#   (Session info: chrome=93.0.4577.63)
# For example, after clicking a "Calcuate Discount" button, or any other UI webDriver
# statement, before execution of the following webDriver statement, Selenium
# will wait at least 5 seconds.
# If all the webElement become available before the waiting time, i.e. in 1.5 seconds,
# then the current webDriver statement is executed right away and everything
#  will be okay because the webelement needed are already available for a successful
#  execution of the current statement. with this explicit_wait() we do not need to use
#  the time.sleep(x) to wait for webdriver command execution.
# if the X seconds pass and the webElement is not available then the target statement
# will fail with a "TimeoutException" error:
# Traceback (most recent call last):
#   File "C:\Users\ssshh\PycharmProjects\HectorFirstpythonProject\SeleniumPythonCode\P06ExplicitWait.py", line 104, in <module>
#     sixSecondsWaitCondition.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span[class='promoInfo']")))
#   File "C:\Users\ssshh\AppData\Local\Programs\Python\Python39\lib\site-packages\selenium\webdriver\support\wait.py", line 80, in until
#     raise TimeoutException(message, screen, stacktrace)
# selenium.common.exceptions.TimeoutException: Message:

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Program start by Searching for some product containing 'ber' in the name, and then adding
# to the shopping cart all the item returned by clicking the 'ADD TO CART" button.

# 1: Search for the product:
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")  # using tagName.className selector.

time.sleep(3)   # Explicitly to wait 3 seconds for the search to return all the products, and avoid an
# error in the next webdriver command that uses any object returned by previous webDriver
# command .send_keys("ber"). Note: this wait could also be explicitly coded in the next
# or below webDriver command to wait the 3 seconds before its own execution. This explicit way
# is coded below in line xxxxxxx

# Below is to count the number of products returned by the search:
print("Number products: ", len(driver.find_elements_by_css_selector("div[class='products'] div[class='product']")))
# also this Xpath locator get the total product returned: "//div[@class='products']/div"

# 2: click on the 'ADD TO CART' button of each product. the button are child of the a div tag
# with class name 'product-action'; so we need to have a locator that locates all the buttons
# of all the products returned by the search, this is "//div[@class='product-action']/button"
# which is a parent/child Xpath location
# create a list object to hold all the buttons:
buttonsList = driver.find_elements_by_xpath("//div[@class='product-action']/button")
# also the parent/child CSS locator can be used: "div[class='product-action'] button[type='button'] "

# 3: Create a for...loop to click on all the buttons
for button in buttonsList:
    button.click()

# 4: Click on the Go to Cart image (CSS locator: "img[alt='Cart']"
driver.find_element_by_css_selector("img[alt='Cart']").click()

# The image opens a popup with the button to click to "Proceed to checkout"
# we have created the Xpath using the text displayed in the button:
#       //button[text()='PROCEED TO CHECKOUT']
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

# 5: The check out process normally take 5 seconds to complete therefore below webdriver statement will
# fail because the ".promoCode" webElement will not be available right away. To avoid this we use the
# Explicit_wait for this webElement using the WebDriverWait() class. this class has two parameters:
# WeDriverWait(the created webDriver object, How many seconds to wait)

sixSecondsWaitCondition = WebDriverWait(driver, 6)  # this will import: (from selenium.webdriver.support.wait import WebDriverWait)
# sixSecondsWaitCondition is an object defined for the driver and specific amount of time to wait. so we can have multiple.

sixSecondsWaitCondition.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))
# the "until" method define the condition to wait for and the specific element to wait for.
# the "expected_conditions" will import the (from selenium.webdriver.support import expected_conditions)
# there are multiple wait condition i.e.: alert_is_present, element_to_be_clickable, title_is,
# element_to_be_selected, text_to_be_present_in_element and more.
# "By." import the class (from selenium.webdriver.common.by import By) which offers multiple
# selector method, i.e. (By.CSS_SELECTOR, ".promoCode") or (By.CLASS_NAME, "promoCode")
# if the webElement in the condition is available in 1.5 second then the webDriver statement is
# executed right away without waiting for the 6 seconds.
# This Explicit wait condition is APPLICABLE ONLY to this webelement (By.CSS_LOCATOR, ".promoCode").
# this is different that the Implicit wait that is applicable to all the webDriver statements in the
# program.

# Now we can use the webElement we were waiting for:
# In the new page, now enter the promo code using the CSS locator based on class "input.promoCode", this
# webDriver statement is executed with the EXPLICIT_wait defined for webElement ".promoCode"
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")

# Click on the "Apply Discount" button: using the class name "promoBtn"
driver.find_element_by_class_name("promoBtn").click()

# the "Apply discount" takes EXACTLY 5 seconds to complete therefore we have to define explicit wait:
sixSecondsWaitCondition.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span[class='promoInfo']")))
# To get the content in Response message, about the status of the discount, use locator "span[class='promoInfo']"
discountStatus = driver.find_element_by_css_selector("span[class='promoInfo']").text
# if we run this program with EXPLICIT WAIT OF 5 seconds, then the above statement
# will fail with a "TimeoutException" error:

# Traceback (most recent call last):
#   File "C:\Users\ssshh\PycharmProjects\HectorFirstpythonProject\SeleniumPythonCode\P06ExplicitWait.py", line 104, in <module>
#     sixSecondsWaitCondition.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span[class='promoInfo']")))
#   File "C:\Users\ssshh\AppData\Local\Programs\Python\Python39\lib\site-packages\selenium\webdriver\support\wait.py", line 80, in until
#     raise TimeoutException(message, screen, stacktrace)
# selenium.common.exceptions.TimeoutException: Message:

# because this webdriver statement waited for 5 seconds before starting execution, and when
# started it was unable to locate the webelement indicated by the selector; because it is
# created by the previous webDriver statement and it takes at exactly 5 second to complete its
# execution and make the webElement available for all others webdriver statements, so the
# solution for this error is to increase the amount of seconds to 6 or higher in the
# EXPLICT WAIT condition defined above: "sixSecondsWaitCondition = WebDriverWait(driver, 6)"

print("Discount Status: ", discountStatus)
# Note the first time above print statement executed is did not printed the content of the
# discount