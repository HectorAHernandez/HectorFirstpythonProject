# WebdDriver Locators In Selenium:
# Locators are used to identify objects/elements in a webpage.
# type of locators and suggested hierarchy in using then:
#    Type           Selenium
#                   Method used to find
#    --------       ------------------
# 1- ID             find_element_by_id()
# 2- Name           find_element_by_name()
# 3- CSS
# 4- Xpath
# 5- ClassName
# 6- linkText

# Customized CSS Syntax:
# tagName[attribute='UniqueValue']  --> tagName is optional
# Regular Expression: [attribute*='value']
# i.e. input[name='email']
# we have to select and attribute having a unique value
# to verify if the CSS selector we have defined, go to the browser Developer section
# that we opened for Inspect the webElement click on the "Console" tab and issue the
# command: 1- for CSS locator: $("CSS Selector to test"). $("tanName[attribute='value']")
    #      2- for Xpath locat: $x(//tagName[@attribute='value']).
# Result:
    # $("input[name='email']")
    # _.fn.init [input.form-control.ng-pristine.ng-invalid.ng-touched, prevObject:_.fn.init(1)]
    # 0: input.form-control.ng-pristine.ng-invalid.ng-touched
    # length: 1  i.e.: ( O -> Not found; 1 --> 1 found this is what we want;  n --> multiple)
    # prevObject: _.fn.init [document]
    # [[Prototype]]: Object(0)
# if the length has the value '1' it means a unique identifier created>
# by hoover on the line 0: input the webelement is highlighted on the page.
# Selenium search for the webElement from top to left, and pass the control/activate
# to the very first one that is found, therefore if the CSS/Xpath used identify no
# a unique element we have to make sure it does.

# Customized Xpath Syntax:
# //tagName[@attribute='UniqueValue']  --> tagName is optional
# Regular Expression //tagName[contains(@attribute,'value')]
# for any tagName, using '*' as Regular Expr.  //*[contains(@attribute,'value')]

# Generating CSS from ID attribute
# tagName#IDofTheAttribute  --> tagName is optional. --> input#username, input#password09
# or #IDofTheAttribute  --> #username, #password09  (this '#' selector is only for the "id" attribute)

# Generating CSS from className attribute
# tagName.clasNameAttribute  --> tagName is optional. --> input.pricename
# or .classNameAttribute  --> .pricename  (This '.' selector in only for the "className" attribute)

# Defining the webDriber object:
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Selenium\\BrowserExecutableFiles\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice")

# The page's HTML code contains the definition of all the tags, attributes and values
# for all webElements in the page. to get this information we use the "Inspector" tool
# in the Developer tool of the browser:
driver.find_element_by_name("name").send_keys("Hector")
# note, once Selenium webDriver find the element on the page it pass control to it
# or activate it so that we can perform any method like ".send_keys" to type in it.
driver.find_element_by_name("email").send_keys("ssshhernandez@gmail.com")

# clicking on a checkbox element:
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

# We can use the id and name attribute to identify a webElement as long as the designer of
# the page used then in the webElement definition. If there is no Id or name to
# identify the webElement then we can use: Xpath and CSS locator tool. Example:
# for the "Submit button" which has this webElemnt definition:
#     <input class="btn btn-success" type="submit" value="Submit">
# we can use:
# for CSS    : "tagname[attribute='value']"  --> "input[type='submit']" OR "input[value='Submit']"
# for Xpath  : "//tagname[@attribute='value']" > "//input[@type='submit']" ^ "//input[@value='Submit']"

# To double check that we have created a unique (only one locator in the page) we can use the
# Console in the browser Developer tool, after the Inspector and enter below commands:
# For CSS:   $("tagName[attribute='value']")
# for Xpath: $x("//tagName[@attribute='value']")

# The Python Selenium webDriver commands for the "Submit" button could be:
#driver.find_element_by_css_selector("input[type='submit']").click()
driver.find_element_by_xpath("//input[@type='submit']").click()

# Note, for general awareness: below the different in the webDriver command:
# Python: driver.find_element_by_css_selector()
# Java   : driver.findElementByCssSelector().

# Using the class tag as a selector, when a class tag contain spaces it means that there are
# multiple classes used, we can use one of them for the selector i.e. "alert-success":
# <div class="alert alert-success alert-dismissible">
#    <a aria-label="close" class="close" data-dismiss="alert" href="#">×</a>
#    <strong>Success!</strong> The Form has been submitted successfully!.
# </div>
# This could be the webDriver command:
message = driver.find_element_by_class_name("alert-success").text
print("completion message: " + message)

# we can use CSS Regular expression to create the selector based on a substring in any attribute of
# any "tag" by adding an '*' after the attribute's name to indicate "contains this substring":
message2 = driver.find_element_by_css_selector("div[class*='alert-success']").text
print("message2: ", message2)
# if the tag name is no needed to uniquely identify the attribute, then the tagName can be omitted:
print("msg3: ", driver.find_element_by_css_selector("[class*='alert-suc']").text)
# Now doing the same thing using Regular expression with Xpath:
print("msg4: ", driver.find_element_by_xpath("//div[contains(@class,'alert-succe')]").text)
# Now using the same Regular expression with '*' to indicate any tagName:
print("Message 5: ", driver.find_element_by_xpath("//*[contains(@class,'alert-succe')]").text)


# Using assert to validate and cancel the process if assertion fail. assert are defining expecting
# to be validated to true, so that the process continue and abend if false.
completionMessage = driver.find_element_by_xpath("//*[contains(@class,'alert-succ')]").text
assert "success" in completionMessage

# Opening another website: Sale force"
driver.get("https://login.salesforce.com/")
# using the '#id' and '.className' as CSS locators:
driver.find_element_by_css_selector("#username").send_keys("hector@gmail.com")
driver.find_element_by_css_selector(".password").send_keys("validpass")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_css_selector("input.password").send_keys("a;lalkj;lk")

# Selenium offer a method to locate a link (tag type 'a') using the visible text in the link:
# they are: ".find_element_by+link_text" and ".find_element_by_partial_link_text"
driver.find_element_by_link_text("Forgot Your Password?").click()
time.sleep(2)
# driver.back()
# driver.find_element_by_partial_link_text("Use Custom Dom").click()

# Generating Xpath bases on any tag that display text on the webpage:
# this only for Xpath. this is the format //tagname[text()='xxxxx']
driver.find_element_by_xpath("//a[text()='Need Help Logging In?']").click()  # open the help page.
time.sleep(2)
driver.back()  # return to previous page
# click on Cancel button to go back to login page:
driver.find_element_by_xpath("//input[@name='cancel']").click()
#driver.find_element_by_css_selector("input[name='cancel']").click()


# Creating Xpath and CSS BY Traversing tags from parent tag to child tag, this is used when the
# child tag does not have a unique way to identify the webelement because it is built in a
# dynamic way.
#       xpath format: //ParentTagName[@attribute='value']/childTagName[x] (/ in between) where x
#       is used if there are more than one child to indicate which one we refer to
print("With Xpath: ", driver.find_element_by_xpath("//div[@id='usernamegroup']/label[1]").text)
# note: When there is only one child, for Xpath it is okay to indicate label[1] for the child; but not for CSS.
# Traveling using Great-grand parent, in case that the gran-parent is not unique:
print("Xpath GreatGrpad: ", driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
# above we used child 1 out of three div children in the form, there are other type of children.

#       CSS format: parentTagName[attribute='value'] childTagName[x] (A space in between, not '/')
print("With CSS: ", driver.find_element_by_css_selector("div[id='usernamegroup'] label").text)
# Traveling using Great-grand parent, in case that the gran-parent is not unique:
print("CSS GreatGrpad: ", driver.find_element_by_css_selector("form[id='login_form'] div[id='usernamegroup'] label").text)

# Now using CSS parent/child to get the text for the password label
print("CSS using 'attribute:nth-child(n)' : ", driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
# Same using Xpath:
print("Xpath for pwd: ", driver.find_element_by_xpath("//form[@name='login']/label").text)
print("OR Xpath for pwd: ", driver.find_element_by_xpath("//form[@name='login']/label[1]").text)

