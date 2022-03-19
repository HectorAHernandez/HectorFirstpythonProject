# this program shows how to check ALL the checkboxes in a checkboxes group:
# 1- identify a common locator, using one of the attributes that has common value for all
#    of the checkboxes.
# 2- Create a list of all the checkboxes.
# 3- For...Loop to click on all the individual checkbox.
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Selenium\\BrowserExecutableFiles\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# 1: identify common locator: in this case the common attribute is "type" with value 'checkbox'
#    therefore the common CSS locator is "input[type='checkbox']"

# 2: Create the list of ALL checkboxes:
checkboxesList = driver.find_elements_by_css_selector("input[type='checkbox']")
print("number of item in checkboxes List is: ", len(checkboxesList))

# 3: For...Loop to click on ALL checkboxes.
for checkbox in checkboxesList:
    # to retrieve the value/content of the 'name' attribute:
    print("'name' attribute value is: ", checkbox.get_attribute("name"))
    # to retrieve the content of the 'value' attribute:
    print("'value' attribute value is: ", checkbox.get_attribute("value"))
    if checkbox.get_attribute("name") != "checkBoxOption1":  # all but checkbox_1
        checkbox.click()  # turn check ON.
        assert checkbox.is_selected()  # verify if the check box was selected.

# to clear(turn OFF) all checkboxes, we just need to click all again.
for checkbox in checkboxesList:
    if checkbox.get_attribute("value") != "option1":
        checkbox.click()
        assert "false" != checkbox.is_selected()  # assert that the checkbox is not selected.

# clicking on checkbox using Xpath with tag=input and attribute=name containing 'Option2'
driver.find_element_by_xpath("//input[contains(@name,'Option2')]").click()
option2Text = driver.find_element_by_xpath("//input[contains(@name,'Option2')]").text

# clicking on checkbox using CSS with tag=input and attribute=value equal to 'option3'
driver.find_element_by_css_selector("input[value='option3']").click()

# Again click on checkbox using attribute  id equal to 'checkBoxOption3' to turn it OFF
driver.find_element_by_id("checkBoxOption3").click()

# Radio button selection: only one option can be selected, this is the last one clicked.
# In this page for the Radio buttons the only attribute having unique content is the 'value'
# attribute, therefore we can create a locator for the specific radio button we want to
# click i.e. "input[value='radio2']"
driver.find_element_by_css_selector("input[value='radio2").click()  # select Radiobutton 2

# or we can make a list of all the radio button using any of the attributes having common
# content i.e. name, class or type:
#       input[class='radioButton']
#       input[type='radio']
#       input[name='radioButton']
radioButtonsList = driver.find_elements_by_css_selector("input[class='radioButton']")
radioButtonsList[2].click()  # Select the 3 radio button

# Using the driver().is_displayed() method: This method works with objects that are defined in
# the HTML even though they are not displayed at a given time, so we use this method to verify
# if the object is displayed on the page and give the result: 'True' OR 'False'
print("Is the text displayed?", driver.find_element_by_css_selector("input[id='displayed-text']").is_displayed())

# assertion for expecting the result is 'True'
assert driver.find_element_by_css_selector("input[id='displayed-text").is_displayed()

# no click on the Hide button to hide the text
driver.find_element_by_id("hide-textbox").click()
print("Now is text displayed?", driver.find_element_by_css_selector("input[id='displayed-text").is_displayed())

# assertion for expecting the result is false. (using assert not)
assert not driver.find_element_by_id("displayed-text").is_displayed()

