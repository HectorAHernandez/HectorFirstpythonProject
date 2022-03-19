# Continuing using Explicit and Implicit Wait. This is going to implement a Functional test where it will be
# validating that the products that are displayed in the first page (clicked to Add to cart) are displayed in
# the second page (check out cart)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Selenium\\BrowserExecutableFiles\\chromedriver.exe")
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Program start by Searching for some product containing 'ber' in the name, and then adding
# to the shopping cart all the item returned by clicking the 'ADD TO CART" button.

# 1: Search for the product:
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")  # using tagName.className selector.

time.sleep(3)   # Explicitly to wait 3 seconds for the search to return all the products, and avoid an
# error in the next webdriver command that uses any object returned by previous webDriver
# command .send_keys("ber"). this time.sleep(3) is a key element in this program to make sure that all the
# returned products/object are available in the page for below codes (For...Loop) that click on the elements.

# Below is to count the number of products returned by the search:
numberProduct = len(driver.find_elements_by_css_selector("div[class='products'] div[class='product']"))
print("Number products: ", numberProduct)
# also this Xpath locator get the total product returned: "//div[@class='products']/div"

# 2: click on the 'ADD TO CART' button of each product. the button are child of the a div tag
# with class name 'product-action'; so we need to have a locator that locates ALL the buttons
# of ALL the products returned by the search, this is "//div[@class='product-action']/button"
# which is a parent/child Xpath location
# create a list object to hold all the buttons:
buttonsList = driver.find_elements_by_xpath("//div[@class='product-action']/button")
# also the parent/child CSS locator can be used: "div[class='product-action'] button[type='button'] "

# Define the Lists to hold the products from product and Cart pages:
productsClickedList = []
productsInCartList = []

# 3: Create a for...loop to click on all the buttons and populate the productsClickedList
i = 0
for buttonItem in buttonsList:
    print("i = ", i+1)     # without the time.sleep(3) above the third button is not longer available and
                            # generate the selenium.common.exceptions.StaleElementReferenceException: Message:
                            # stale element reference: element is not attached to the page document
    i = i + 1
    prodName1 = buttonItem.find_element_by_xpath("parent::div/parent::div/h4").text
    print("product name1: ", prodName1)

    productsClickedList.append(buttonItem.find_element_by_xpath("parent::div/parent::div/h4").text)  #Add product to list
    buttonItem.click()

print("productsClickedList: ", productsClickedList)

# 3.1 New Code: One way to get the name of all the product in first page is to create a list of them similar to
# the above buttonsList, as follow; but later we will code a second way using the for...loop already created for
# creating the buttonsList
# way 1:
prodsListTest = driver.find_elements_by_css_selector("h4[class='product-name']")
for product in prodsListTest:
    prodNameTest = product.text
    print("prodNameTest:", prodNameTest)

# Way 2: The 'h4' tag which contains the product name is a child of the 'div' tag 'product-image' in the 'div' product.
#        The 'button' tag is a child of the 'div' tag 'product-action' in the 'div' product.
#        because both are under the same grand parent ('div' product) we can use Xpath parent/child traversing to go
# from the button tag to the grand parent ('div' product) and then to the child ('div' product-image) and here get the
# child 'h4' with the product name. All of this in the for...loop for the button. This meant that we can start the
# traversing using button.find_element_by.... instead of from the top (driver.find_element_by....).
# We can traverse back only using Xpath, CSS does NOT have this capability. the Xpath for the child button is:
# //div[@class='product-action']/button to go to it parent we add the /parent::  (two columns)
# //div[@class='product-action']/button/parent::  now adding the tag of this child parent (div, in this case)
# //div[@class='product-action']/button/parent::div  now adding the tag of this child parent (div, in this case)
# //div[@class='product-action']/button/parent::div/parent::div  added that tab of the grand parent.
# //div[@class='product-action']/button/parent::div/parent::div/h4 added the h4 tag which contains the product name.
# so the final Xpath to traverse back to get the product's name from the button object is:
# //div[@class='product-action']/button/parent::div/parent::div/h4
# because we already are in the button object we can omit the part of it in the Xpath and only use this:
# parent::div/parent::div/h4    (this is  button.find_element_by_xpath("parent::div/parent::div/h4")
# go back to the for...loop for button and see "productName1 = button.find_element_by_xpath("parent::div/parent::div/h4").text"



# 4: Click on the Go to Cart image (CSS locator: "img[alt='Cart']"
driver.find_element_by_css_selector("img[alt='Cart']").click()

# The image opens a popup with the button to click to "Proceed to checkout"
# we have created the Xpath using the text displayed in the button:
#       //button[text()='PROCEED TO CHECKOUT']
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

# 5: The check out process normally take 5 seconds to complete.
waitCondition = WebDriverWait(driver, 6)  # this will import: (from selenium.webdriver.support.wait import WebDriverWait)
# sixSecondsWaitCondition is an object defined for the driver and specific amount of time to wait. so we can have multiple.

waitCondition.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))

# In the new page, now enter the promo code using the CSS locator based on class "input.promoCode", this
# webDriver statement is executed with the EXPLICIT_wait defined for webElement ".promoCode"
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")

# 6: Populate the list productsInCartList:
productsInCart = driver.find_elements_by_css_selector("p.product-name")
for productInCart in productsInCart:
    productsInCartList.append(productInCart.text)

print("productsInCartList: ", productsInCartList)

# 7: compare the product lists
assert productsClickedList == productsInCartList

# Save the original amount before discount:
orignalAmount = driver.find_element_by_css_selector(".discountAmt").text
print("orignalAmount: ", orignalAmount, float(orignalAmount))

# Click on the "Apply Discount" button: using the class name "promoBtn"
driver.find_element_by_class_name("promoBtn").click()

# the "Apply discount" takes EXACTLY 5 seconds to complete therefore we have to define explicit wait:
waitCondition.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span[class='promoInfo']")))
# To get the content in Response message, about the status of the discount, use locator "span[class='promoInfo']"
discountStatus = driver.find_element_by_css_selector("span[class='promoInfo']").text
print("Discount Status: ", discountStatus)

# Now to validate the value of the discounted amount is less than the original amount:
discountedAmount = driver.find_element_by_css_selector(".discountAmt").text
print("discountedAmount: ", discountedAmount, float(discountedAmount))


if discountStatus == "Code applied ..!":
    print("Discounted < Original ? : ", float(discountedAmount), " < ", float(orignalAmount))
    assert float(discountedAmount) < float(orignalAmount)  # converting from text/string to number for comparison
    print("*** Discount Applied successfully  ***")
else:
    print("*** Discount NOT Applied ***")

# Now to compare that the Sum of all Total charge column is equal to the Order Total Amount:
# create a list with all the objects in total column of the table.
chargesList = driver.find_elements_by_css_selector("tbody td:nth-child(5)")  # others: "td:nth-child(5) p" and "//tr/td[5]/p"
# sum the each in the list
totalCharge = 0
for charge in chargesList:
    totalCharge = totalCharge + int(charge.text)

print("total Charge: ", totalCharge)

# get the value of Order total charge from the shopping cart page:
orderTotalAmount = int(driver.find_element_by_css_selector(".totAmt").text)
print("orderTotalAmount: ", orderTotalAmount)

assert orderTotalAmount == totalCharge