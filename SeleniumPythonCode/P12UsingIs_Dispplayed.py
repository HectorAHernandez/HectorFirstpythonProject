# this program shows how to use the driver().is_displayed() method:.
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Selenium\\BrowserExecutableFiles\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


# Using the driver().is_displayed() method: This method works with objects that are defined in
# the HTML even though they are not displayed at a given time, so we use this method to verify
# if the object is displayed on the page and give the result: 'True' OR 'False'
print("Is the text displayed?", driver.find_element_by_css_selector("input[id='displayed-text']").is_displayed())

# When the webpage is displayed the field is displayed by default.
# assertion for expecting the result is 'True'
assert driver.find_element_by_css_selector("input[id='displayed-text").is_displayed()

# Now click on the Hide button to hide the text
driver.find_element_by_id("hide-textbox").click()
print("Now is text displayed?", driver.find_element_by_css_selector("input[id='displayed-text").is_displayed())

# assertion for expecting the result is false. (using assert not)
assert not driver.find_element_by_id("displayed-text").is_displayed()
# OR:
assert not driver.find_element_by_id("displayed-text").is_displayed() == "True"

