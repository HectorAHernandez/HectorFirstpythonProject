# the idea of exceptions handling is to throw an error message when expected
# conditions are not met. Python has two mechanisims that allow to throw the
# error: the "raise" and "assert" commands:
# 1- raise command:
#   On a sell product website, the customer has put 2 products in the shopping
#   cart; if at ordering time the cart has a different value than 2 an error
#   message must be raise:

shoppingCart = 0
# other code in the program ....

if shoppingCart != 2:
    raise Exception("Product's count NOT MATCHING shopping Cart count")
    pass  # commented out the raise command to allow execution of below code.

# 2- assert command:
#   assert command evaluate a condition and fail the program execution if the
#   condition is not evauated to True:

assert (shoppingCart == 2)