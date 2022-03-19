# define the print_hi function
def print_hi(parm_01):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {parm_01}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
print(" ** The value of variable __name__ is: ", __name__)
# we are in the P08UseOf__name__variable.py program, when it start execution
# the vary first execute step is to initialize the variable __name__ with
# the value "__main__", therefore the above print() will print "__main__"
# if from this program we call execution of another imported program/function
# the the content of the __name__ variable will change to the name of the
# called program.
if __name__ == '__main__':
    print_hi('Hector Master in PyCharm')  # print_hi is a function
    print("** we are in the main/parent program, this is why the  ")
