# this covers the child windows and tab with Selenium.
# When we click a link and it displays a new window or tab, then Selenium treat them as a child window.
# The driver object that we create only have knowledge or track of the original/initial page where it
# was instantiated/created. This means that when a new window or tab is triggered the driver object
# does not know about it and it's attributes and objects. Therefore we will need to switch to that new
# window/tab to have access to their objects using the "driver.switch_to.window" command.
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Selenium\\BrowserExecutableFiles\\chromedriver.exe")

driver.get("http://the-internet.herokuapp.com/windows")

# click on the 'Click Here' link to open the new window
driver.find_element_by_link_text("Click Here").click()

# A new windows is opened, now if I try to get the text in the h3 tag of this new page (h3=New window)
# then the h3 content off the Parent page will be displayed (h3=Opening a new window),
print("1- After child window, the h3 tag text is for the Parent window: ", driver.find_element_by_tag_name("h3").text)

# note: to use the find_element_by_tag_name() method, the tag must be unique, or only one tag of this
# type in the page (BTW, this is very unusual)

# To access the objects in the child window we have to switch the focus of the driver object to
# the child window by using the driver.switch_to.window("windowID") command.
# To get the windowID value we use the "driver.window_handles[x]" List. this window_handle List keep
# track of all the windows that have been opened during this automation program. In this list the
# index [0] always is for the Main parent Page, and all subsequent index are for the new child windows/tab
# that are opened. The List store this attributes: ("parentID","ChildId")
childWindow_01 = driver.window_handles[1]
print("main parent windowId: ", driver.window_handles[0])
print("childWindow_01 = ", childWindow_01)

# now using the windowID (childWindow_01) we can switch to it:
driver.switch_to.window(childWindow_01)

# now we can use all the objects in the child window.
# now the driver object has access to all object in the child window ONLY (it disconnect from the parent one)
print("2- now the child window h3 tag is 'New Window ' = ", driver.find_element_by_tag_name("h3").text)

# After finishing processing the child window we have to close it with driver.close() method:
driver.close()

# To have access to the parent window/tab objects we have to get back to the parent window using switch_to
# with (index=0):
driver.switch_to.window((driver.window_handles[0]))

print("3- switching to the parent window h3 is: ", driver.find_element_by_tag_name("h3").text)

assert driver.find_element_by_tag_name("h3").text == "Opening a new window"