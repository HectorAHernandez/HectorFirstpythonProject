from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Selenium\\BrowserExecutableFiles\\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/iframe")

# identify the locator for the object to type information: when using ChroPath to create/test the
# locator, ChroPath indicate that the spyed object "body[id='tinymce']" is inside an "iframe" object

# driver.find_element_by_css_selector("body[id='tinymce']").clear()  # to clear the content of the object
# when running this part of the program, Selenium will generate this error:
#       selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to
#       locate element: {"method":"css selector","selector":"body[id='tinymce']"}
# Even though we have a valid locator the element cannot be located because it is defined inside a frame
# object and for the driver.xx object to have access to the objects defined in a frame/iframe/frameset
# we need to use the driver.switch_to.frame() method. The frame code/object come on top of the HTML code
# this is the reason why the driver.xx object cannot find the frame objects.
# Another way to identify if the target object belong to a frame is to verify if the frame/iframe/frameset
# tags are used as part of the parent/grand parent of the element.
# frame/iframe/frameset object can be identified by id, frame name or index (in the order in the page 0, 1, 2...)
# so let comment out above statement: driver.find_element_by_css_selector("body[id='tinymce']").clear()
# and switch to the frame and then execute the statement:
driver.switch_to.frame("mce_0_ifr")  # using the frame id as locator.
driver.find_element_by_css_selector("body[id='tinymce']").clear()

# now provision a value into the frame object:
driver.find_element_by_id("tinymce").send_keys(" *** sucessful ***")

# now if we try to access the 'h3' tag that is outside of the frame we will have same error. therefore
# after finishing processing all the objects in the frame we have to switch back to the default content
# using the method: 'driver.switch_to.default_content()' and then use all the objects that are outside
# of the frame definition:
driver.switch_to.default_content()
print("h3 header is: ", driver.find_element_by_tag_name("h3").text)
