# This program covers Mouse Hovering Action and Others Actions Chain Browser Mouse functionalities.
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Selenium\\BrowserExecutableFiles\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# create an object for Actions Chain class.
hhAction = ActionChains(driver)  # now this hhAction object can perform operation/actions on top
                                 # of the driver object.

# To open the menu, we have to hover over the "Mouse Hover" menu we have to move the cursor to
# the "Mouse Hover" menu (implemented in a button) this could be done in two ways:
# 1:
hhAction.move_to_element(driver.find_element_by_css_selector("button[id='mousehover']")).perform()
# the move_to_element() method, uses a driver's WebElement object, i.e. a button in this case
# 2:
specialMenu = driver.find_element_by_css_selector("button[id='mousehover']")
# then:
hhAction.move_to_element(specialMenu).perform()
# the Chain of ACTIONS has the perform() method as mandatory, so that the action can be performed. so
# only after the perform() is indicated any action will be executed.

# once the menu is opened we can move to the driver's webElement containing the options: :Top" and "Reload"
webElementForOptionTop = driver.find_element_by_link_text("Top")
hhAction.move_to_element(webElementForOptionTop).click().perform()
