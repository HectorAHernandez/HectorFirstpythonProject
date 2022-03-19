# this program cover making selection from the different types of dropdonwn fields:
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Selenium\\BrowserExecutableFiles\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice")


driver.find_element_by_name("name").send_keys("Hector")
driver.find_element_by_name("email").send_keys("ssshhernandez@gmail.com")
driver.find_element_by_id("exampleCheck1").click()


# Static Dropdown List handling:
# Selenium WebDriver has a special class called "Select" (with uppercase 'S') which provides all the methods to
# handle the options in the dropdown list fields/object. This Select class can only be used if the
# tagname of the html webpage object is "select".
# To use these methods we have to create/instantiate an object of this Select class as follow:
genderDropDown = Select(driver.find_element_by_id("exampleFormControlSelect1"))  # the id attribute

# used as the locator of the gender dropdown object in the webpage.
# the first time using the select() class we will be prompted to import it from
# (selenium.webdriver.support.select import Select)
# now using the methods in the created object we can select the option we want using the method we want:

genderDropDown.select_by_visible_text("Female")
time.sleep(1)
genderDropDown.select_by_index(0)  # the index of the options, starting in 0, 1, 2 ... n-1 0=Male.

# The Paython Selenium webDriver commands for the "Submit" button could be:
driver.find_element_by_css_selector("input[type='submit']").click()
#driver.find_element_by_xpath("//input[@type='submit']").click()


# Dynamic Dropdown List handling process:
# 1- start typing in the dynamic dropdown field: ind..
# wait 2 seconds for the list to appear, so we can grab the list locator.
# 2- Get common locator that hold all the items that were displayed: the 3 options/countries in the list.
# 3- use the locator to with find_elements (in plural) to create a list with all options/countries.
# 4- Use a For...Loop to click/make a click to make the Selection on the option/country we want from the list.
# 5- Verify the selection we made is now in the dropdown field

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

# 1: Get the locator of the element to start typing:
driver.find_element_by_id("autosuggest").send_keys("united")
time.sleep(2)
# 2: Find a locator common to all the options listed in the dropDown object. To that after
# manually start typing, in order to spy on the list, right click and then select the browser's
# Inspector to get the locator that hold all the option: the 'li' tag contains the list items and
# in each 'li' the 'a' (anchor) tag contains the 'text' that is displayed in the list and that
# we want to select: so the locator for this list of 'a' tags is: "li[class='ui-menu-item'] a"

# 3: use a common locator that return all the options in the dropdown list, so that we can
# create the list of countries returned.
countriesDropDownList = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print("The number of countries found is: ", len(countriesDropDownList))

# 4: For...loop to make the selection by clicking on the li[a] object or option:
for countryItem in countriesDropDownList:
    if countryItem.text == "United States (USA)":
        clickedSelection = countryItem.text
        print("Selection made: ", countryItem.text)  # Printed now because after click it's value is gone.
        countryItem.click()  # Make the selection by clicking on the li[a] object.
        break

# 5: to verify if the selection was correct, we normally try to get the content (objectxx.text) of
# the typing field after the selection we made, normally we would tend to issue
# the WRONG command: driver.find_element_by_id("autosuggest").text; but this is
# wrong because Selenium load the page DOM when it opens the page and the update we made to
# the page, with the dynamic dropdown selection, was done after page was loaded, so Selenium
# does not know of this update until the page is refreshed or loaded again. The update is
# kept in the content of the attribute "value" in the DOM, which has the current value of the object, to get
# this value we use the method "object.get_attribute('value') which returns the content
# of the object's value attribute i.e.:
currentSelection = driver.find_element_by_id("autosuggest").get_attribute('value')
print("Current selected country: ", currentSelection)
# now the assertion:
assert currentSelection == clickedSelection

# to make the above process generic using a variable with as parameter with the country name
# to search in the dynamic dropdown list, see below code:
# 0: Received the parameters:
parmToSelect = "Russian Federation"
parmInputFieldLocator = "autosuggest"
# parmOptionsListLocator = "li[class='ui-menu-item'] a"
parmOptionsListLocator = "//li[@class='ui-menu-item']/a"

# 1: Get the input locator, clear any value in it, and type the value in the parameter
driver.find_element_by_id(parmInputFieldLocator).clear()
driver.find_element_by_id(parmInputFieldLocator).send_keys(parmToSelect)
time.sleep(2)

# 2: the optionList CSS locator is: "li[class='ui-menu-item'] a"

# 3: Create the optionsList
if "//" in parmOptionsListLocator:
    optionsList = driver.find_elements_by_xpath(parmOptionsListLocator)
else:
    optionsList = driver.find_elements_by_css_selector(parmOptionsListLocator)

# 4: For...Loop to click on the option
for option in optionsList:
    if option.text == parmToSelect:
        clickedOption = option.text
        print("clicked option is: ", clickedOption)
        option.click()
        break

# 5: Assert if selected option was the clicked one.
selectedOption = driver.find_element_by_id(parmInputFieldLocator).get_attribute('value')
print("select Option is: ", selectedOption)
assert selectedOption == clickedOption



