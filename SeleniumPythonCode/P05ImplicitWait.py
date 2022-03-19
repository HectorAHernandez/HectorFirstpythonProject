# This program show how to use the Implicit Wait. This is useful when we
# have an application that needs to wait for a response before the program continue execution of
# a webDriver statement,
# i.e. A Product sale application that at the shopping cart level, when clicking for applying
# a discount the application has to wait to see if the discount was successfully approved.
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Selenium\\BrowserExecutableFiles\\chromedriver.exe")

driver.implicitly_wait(5)  # this implicit wait Globally to all webdriver commands, and
#  indicates that, before starting execution of all webDriver statement, wait for 5 (x) seconds. This
#  waiting time is for giving time for all webElements required for the execution (that normally are
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
# then the current webDriver statment is executed right away and everything
#  will be okay because all webelements needed are already available for a successful
#  execution of the current statement. with this implicit_wait() we donot need to use
#  the time.sleep(x) to wait for webdriver command execution.

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

#time.sleep(2)
# 4: In the new page, now enter the promo code using the CSS locator based on class "input.promoCode"
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")

# Click on the "Apply Discount" button: using the class name "promoBtn"
driver.find_element_by_class_name("promoBtn").click()

# To get the content in Response message, about the status of the discount, use locator "span[class='promoInfo']"
discountStatus = driver.find_element_by_css_selector("span[class='promoInfo']").text
# if we run this program with driver.implicit_wait(4), 4 seconds, then the above statement
# will fail with error:
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate
# element: {"method":"css selector","selector":"span[class='promoInfo']"}
# because this webdriver statement waited for 4 seconds before starting execution, and when
# started it was unable to locate the webelement indicated by the selector; because it is
# created by the previous webDriver statement and it takes at least 5 second to complete its
# execution and make the webElement available for all others webdriver statements, so the
# solution for this error is to increase the amount of seconds to 5 or higher in the
# implicit_wait(5).

print("Discount Status: ", discountStatus)
# Note the first time above print statement executed is did not printed the content of the
# discount