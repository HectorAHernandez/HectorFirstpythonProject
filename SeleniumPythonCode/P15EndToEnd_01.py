# This is the first program for the functional End To End test.
# This program:
# 1- Click on the Shop Link.
# 2- Click on the Shopping cart button to add a product to the shopping cart
# 3- Click on the Checkout button to go to the shopping cart
# 4- validate the product in the shopping cart
# 5- if selected product is in the shopping cart then click on the Checkout button.
# 6- type the delivery country location
# 7- to select the country:
# 8- Define explicit wait for the list of country to popup:
# 9- after list of country popped up, create countriesList
# 10- loop the countriesList to click the desired country:
# 11- click on the 'I agree' checkbox
# 12- Click on the Purchase button:
# 13- to grab the value in the response message displayed, which is NOT a real alert that we can switch_to:
# 14- now we can use Selenium to take a screenshot of the page with the successful message.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

browserOptionsObject = webdriver.ChromeOptions()
browserOptionsObject.add_argument("--start-maximized")
# browserOptionsObject.add_argument(("headless"))
browserOptionsObject.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="C:\\Selenium\\BrowserExecutableFiles\\chromedriver.exe",
                          options=browserOptionsObject)
driver.implicitly_wait(5)  # Implicit wait applicable to all webDriver commands.

# start defining an Explicit wait:
sixSecondsWaitCondition = WebDriverWait(driver, 6)   # Explicit wait applicable to certain webDriver command.

driver.get("https://rahulshettyacademy.com/angularpractice/")
print("Page title:", driver.title)

# initialize productToSelect:
productToSelect = "nokia"
productFound = False
nameProductInSC = ""

# click on the Shop link.
driver.find_element_by_css_selector("a[href*='shop']").click()

# 1: Build a list of all the products displayed:
productsList = driver.find_elements_by_css_selector("div[class='card h-100']")  # or //div[@class='card h-100']

for productItem in productsList:
    print("Whole product Object in List:", productItem.text)

    # product contains the CSS path for the iterated productItem "div[class='card h-100']" as a parent
    # and now we have access to the CSS selector or Xpath of the children by using the productItem object
    productName = productItem.find_element_by_css_selector("div h4 a").text  # "div h4 a" OR "div/h4/a"
    # instead of the whole path "div[class ='card h-100'] h4 a" OR //div[@class='card h-100']/div/h4/a"
    # because productItem points to the parent part of the path.
    # Note: in the Xpath DO NOT start with '//', as normal, because it will start searching/traversing
    # from the top of the page; and we just need to continue from the position already in the parent.

    print("productName:", productName)

    if productToSelect.upper() in productName.upper():
        # Add product into cart.
        productItem.find_element_by_css_selector("div button").click()  # or "div[2]/button"  or
        # "div/button" because the button object is unique only in all the 'div' below the parent.

        # Open the Shopping cart page by clicking the shopping cart button:
        driver.find_element_by_css_selector("a[class*='btn-primary']").click()  # or
        # "//a[contains(@class,'btn-primary')]"

        # create a list with all the products in the shopping cart.
        # productsInShoppingCart = driver.find_elements_by_css_selector("tbody tr")
        productsInShoppingCart = driver.find_elements_by_xpath("//tbody/tr")

        # Loop to identify webElement/objects in the shopping cart.
        for productInShoppingCart in productsInShoppingCart:
            print("Whole product Object In Shopping Cart List: ", productInShoppingCart.text)

            print("*****: ", productInShoppingCart.find_element_by_xpath("td[1]").text)
            # in the shopping cart list, there are two lines that are not for product (total and a message) both of them
            # have the value '&nbsp;' in the first 'td' child tag. this value indicate "non braking space" to the HTML;
            # but in Selenium-Python code we treat it as single space "1". Therefore below 'if' avoid that the error:
            # "selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate
            # element: {"method":"xpath","selector":"td[1]/div[@class='media']/div/h4/a"}" in the next webDriver command
            # to be executed (line 65 or 66), because these two rows do not have the element indicated there.
            if productInShoppingCart.find_element_by_xpath("td[1]").text != " ":  # This is the value in the HTML
                # code "&nbsp;", it is equal one space "1".

                # identify the name of the product
                # nameProductInSC = productInShoppingCart.find_element_by_css_selector
                #                                                               ("td div[class='media'] div h4 a").text
                nameProductInSC = productInShoppingCart.find_element_by_xpath("td[1]/div[@class='media']/div/h4/a").text
                print("nameProductInSC:", nameProductInSC)
                if productToSelect.upper() in nameProductInSC.upper():

                    assert nameProductInSC == productName

                    # Get the Quantity for the product in the Shopping Cart
                    # quantityInSC = productInShoppingCart.find_element_by_css_selector
                    #                                                               ("td input").get_attribute("value")
                    quantityInSC = productInShoppingCart.find_element_by_xpath("td/input").get_attribute("value")
                    print("quantityInSC", quantityInSC)

                    # Get the Price for the product in the Shopping Cart
                    priceInSC = productInShoppingCart.find_element_by_xpath("td[3]/strong").text
                    wkList = priceInSC.split(".")
                    priceInSC = wkList[1]
                    print("priceInSC:", priceInSC)

                    # Get the Total charge for the product in the Shopping Cart
                    totalInSC = productInShoppingCart.find_element_by_xpath("td[4]/strong").text
                    wkList = totalInSC.split(".")
                    totalInSC = wkList[1]
                    print("totalInSC", totalInSC)

                    assert int(totalInSC) == (int(quantityInSC) * int(priceInSC))
                    productFound = True
                else:
                    continue
            else:
                continue
        break
    else:
        continue

if productFound:

    # click on the 'Checkout' button
    driver.find_element_by_css_selector("button[class*='btn-succe']").click()

    # type the delivery country location
    deliveryCountry = "united states of america"
    driver.find_element_by_id("country").send_keys(deliveryCountry)

    # to select the country:
    # Define explicit wait for the list of country to popup:
    sixSecondsWaitCondition.until(expected_conditions.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div[class='suggestions'] ul li a")))

    # after list of country popped up, create countriesList
    countriesList = driver.find_elements_by_css_selector("div[class='suggestions'] ul li a")

    # loop the countriesList to click the desired country:
    for country in countriesList:
        if country.text.upper() == deliveryCountry.upper():
            country.click()

    # click on the 'I agree' checkbox
    driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']/input[@id='checkbox2']").click()
    #driver.find_element_by_css_selector("div[class*='checkbox checkbox-primary']").click()
    #driver.find_element_by_css_selector("input[id='checkbox2']").click()
    # notes: this radio button was not able to be located by using the id = checkbox2 with find_element_by_id or
    # even any one using the 'input' tag. Only successful when using the 'div' tag to identify the checkbox. This
    # error is generated:
    # selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element
    #         <input id="checkbox2" type="checkbox"> is not clickable at point (720, 243). Other element would
    #         receive the click: <label for="checkbox2">...</label>

    # Click on the Purchase button:
    driver.find_element_by_css_selector("input[value='Purchase']").click()

    # to grab the value in the response message displayed, which is NOT a real alert that we can switch_to:
    alertMessage = driver.find_element_by_class_name("alert-success")
    print("*** Alert Message:", alertMessage.text)

    # now we can use Selenium to take a screenshot of the page with the successful message.
    driver.get_screenshot_as_file("finalScreenshot.png")  # this will be save in the project's root directory
    # note: we only take screenshot when one assertion fails, to help with the trouble shooting.

    print(" --- Product ", nameProductInSC, "Found ---")
else:
    print(" --- Product ", productToSelect, " NOT Found ---")
