# To generate the PyTest testCases execution report in html we have to install the Pytest HTML report package
# using the command: pip install pytest-html
# then we have to run the PyTest.py program with have to add the flag --html=reportName to the
# command to execute the pyTest.py, in the command prompt console:
# py.test pyTestName.py --html=reportName.html -s -v
# example:
# C:\Users\ssshh\PycharmProjects\HectorFirstpythonProject\usingPyTestDemo>py.test -s -v
#     test_08DataDrivenParametersWrappedInClass.py --html=test01ExecReport.html

# or to generate the html report in a "Report Directory" created in the project:
# C:\Users\ssshh\PycharmProjects\HectorFirstpythonProject\usingPyTestDemo>py.test -s -v
#     test_08DataDrivenParametersWrappedInClass.py
#     --html=C:\Users\ssshh\PycharmProjects\HectorFirstpythonProject\usingPyTestDemo\ExecutionHTMLReports\test01ExecReport.html

# after execution the html report will be place in the project root directory under the name:
# test01ExecReport.html.
# Now to see the report we can:
# 1- Refresh the project clicking on option "Reload from disk"
# 2- Right click on the report's name and click on the "Copy Path/Reference..."
# 3- Paste the copied path into a browser URL and click enter to view the report.

# so far, with above flag --html=reportName.html, NO Log is added to the html report. To add logs
# we have to....