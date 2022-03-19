# This program covers the mouse actions: double click and right click:
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Selenium\\BrowserExecutableFiles\\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
mouseAction = ActionChains(driver)

# now to Right click on the any webElement object
mouseAction.context_click(driver.find_element_by_css_selector("#double-click")).perform()

# below perform the mouse double click action:
mouseAction.double_click(driver.find_element_by_id("double-click")).perform()

# switch to the generated alert to take the message and click okay (accept()) it.
alertObject = driver.switch_to.alert
alertMessage = alertObject.text     # use the content of the alert.
print("alertMessage: ", alertMessage)
assert alertMessage == "You double clicked me!!!, You got to be kidding me"
alertObject.accept()    # click OK button with this method.

