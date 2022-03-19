# JavaScript Executor is used to identify objects in the webPage that are not easily accessible
# by Selenium WebDriver.
# The HTML DOM document object is the owner of All webelements or objects that are defined in the page.
# The Document Object Model (DOM) is a JavaScript API for HTML and XML documents. The DOM defines the logical
# structure of documents and the way a document is accessed and manipulated. The DOM is designed to
# be used by programming languages like, Java, Python...
# We can access any webelement/object in an HTML page by using the "document" object of the page, this
# is in the browser Inspector go to the Console tab and use the document.method() object to use
# all the methods available for the document object, i.e:
#       document.getElementsById, document.getElementsByName, getElementsByTagName..
# note that the method name is in plural, which means that a list will be returned and we will need
# to use the index [x] to point the element we want:


# JavaScript DOM can access any webElement on the web page just like Selenium does, and more.
# Selenium have a method to execute JavaScript code to access any element in the webpage and also
# to execute any javaScript code. We need to execute this JavaScript code to access certain
# webelements in the page that are not easy accessible by Selenium webDriver. This is Selenium
# WebDriver is allowing this door open for used when needed.
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Selenium\\BrowserExecutableFiles\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
# now sending the 'Hector King' value to the 'name' object in the page:
driver.find_element_by_css_selector("input[name='name']").send_keys("Hector King")
# note: there are two webelements in the page using the same input tag with name attribute = 'name'
# therefore the value 'Hector King' will be typed in both of them.


# trying to get the value sent by this automation program to the 'name' object:
nameOnPage = driver.find_element_by_css_selector("input[name='name']").text
print("nameOnPage", nameOnPage)
# the content of the 'nameOnPage' variable was/is empty because with  the '.text' method we can
# only get content/value created/moved when the DOM loaded/refreshed the page, not the values
# moved/type/created with the automation program. We have two ways of getting the data moved by
# the program
# way # 1: using the '.get_attribute('value') method, to get the value of the attribute value of the
# the webelement. Even though the developer did not define the 'value' attribute for the
# webelement, the DOM will always keep the current value of the object in this 'value' attribute:
nameOnPage = driver.find_element_by_css_selector("input[name='name']").get_attribute("value")
print("nameOnPage after using 'value' attribute: ", nameOnPage)
# way #2: using the driver.execute_script() method to use a DOM JavaScript command to locate the webelement.
# Selenium gives/passes the control to whatever command we pass inside the argument of the
# .execute_script() method
nameOnPageJavaScript = driver.execute_script("return document.getElementsByName('name')[0].value")
# we executed the 'return' JavaScript command to return the value of the webElement 'name'
print("nameOnPageJavaScript: ", nameOnPageJavaScript)

# Now trying to click on the "Shop" link to go to the Shop page
driver.find_element_by_css_selector("a[href*='shop']").click()
# For Selenium to be able to click on any object it must be completely visible, another pop-up, or
# overlapping link/menu option can block the button to be completely visible. In this situation we
# can click executing the .execute_script() method  to reach to it using DOM command.
# assuming that the above link webelement is blocked. "a[href*='shop']" the error message:
# "Element cannot be clickable" is displayed when we try to click it. So below the solution:
shopLink = driver.find_element_by_css_selector("a[href*='shop']")  # Grab the element we want to click.
homeLink = driver.find_element_by_xpath("//a[text()='Home']")
# driver.execute_script("arguments[x].click();", targetWebObject_0,targetWebObject_1, targetWebObject_2...)
# where:
# "arguments[x].operation();" is a JavaScript command to execute the 'operation' on the targetObject
# indicated in the index [x] : 0 --> targetWebObject_0, 1 --> targetWebObject_1...,
# the semicolon ';' is needed because it is a Java command indicated to execute.
# to click the shopLink we use the index = 0
#driver.execute_script("arguments[0].click();", shopLink, homeLink)

# Or to go back and click the homeLink we use index = 1
#driver.execute_script("arguments[1].click();", shopLink, homeLink)
driver.execute_script("arguments[0].click();", homeLink)

# Scroll down a page:
# Selenium does not have the capability to scroll down a page, therefore we have to use this
# .exectue_script() method, this is used when we are processing a large page where part of the
# webelements become not visible, so we need to scroll down the page to make them visible.
# This W3 School page contains examples of window.scrollTo() method: https://www.w3schools.com/jsref/met_win_scrollto.asp
# to scroll from Top to bottom this is the command:
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
