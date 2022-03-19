# This program re-uses the myFunction() defined in another script, for example P09Use__name__varUtilitiesProgs.py,
# we can import P09Use__name__varUtilitiesProgs.py as a module with below command:


# this is not working: from P09Use__name__varUtilitiesProgs import myfunction as utilitiesProg
import P09Use__name__varUtilitiesProgs as utilitiesProg



utilitiesProg.myfunction()  # calling the method from the imported program.


# When starting running this program the __name__ variable is set to __main__. By importing P09Use__name__varUtilitiesProgs,
# Python starts looking for a file by adding .py to the module name. It then runs the code contained in the imported file.
# But this time it is set to P09Use__name__varUtilitiesProgs to the "__name__" variable. All the commands in this called
# program start execution, this is why line 30:
#      (print("00 - Entering the Utilities program: the value of variable __name__ is " + __name__)
# was executed but not line 34 because the condition, in line 31, was evaluates to false and main() method is not called.
# In this script (P10Use__name__varMainProg.py) we call myFunction() (line 9) which outputs P09Use__name__varUtilitiesProgs.

