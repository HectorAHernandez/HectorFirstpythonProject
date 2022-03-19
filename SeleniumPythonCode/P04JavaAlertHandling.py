# This program handle Alerts. Alerts normally are Java code that displays a popup screen which
# is not in HTML DOM document, therefore cannot be directly handle by the Selenium
# webDriver class. To handle them, we have to use the Selenium webDriver method "switch_to"
# and then indicate the target as "alert", this is:
#           driver.switch_to.alert
# when to the focus is switched to the alert we cannot execute any statement that can break
# this focus before the alert is responded as accepted or dismissed; i.e. the
# print() statement is an Input/Output statement and disconnect the focus on the alert.

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Selenium\\BrowserExecutableFiles\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# this sample program will type text in variable on the screen then click the 'Alert' button
# to display the alert, verify that the typed text is included in the alert and then
# accepting the alert to close it as a positive result/Ok (button).
nameToDisplay = "hector"
driver.find_element_by_id("name").send_keys(nameToDisplay)  # type into the field
driver.find_element_by_css_selector("input[id='alertbtn']").click()  # To display the Alert


# now to be able to access the content of the displayed alert we have to use the
# method 'switch_to' and the target 'alert' and assign its content to an object:
firstAlert = driver.switch_to.alert
print("Alert content: ", firstAlert.text)
assert nameToDisplay in firstAlert.text
firstAlert.accept()
# note while the alert is ACTIVE/ON never use the time.sleep(), because the control is lost
# and the program go to a endless/ no return.

# An alert can have two choices for responding the alert:
# accept() : Yes, Ok, Accept, Agree
# dismiss(): Not, Cancel, Reject...
# below code trigger an alert and based on part the content of the alert accept or dismiss it
driver.find_element_by_id("confirmbtn").click()  # trigger the alert.
secondAlert = driver.switch_to.alert  # retrieve the alert content.
if "Are you sure you want to confirm?" in secondAlert.text:
   secondAlert.accept()
   print("Alert Accepted")  # this statement after responding the alert to avoid change if focus
else:
    secondAlert.dismiss()
    print("Alert dismissed")

