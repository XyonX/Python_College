"""

Write a code in Python using function call to perform division and return
exponent and remainder of division to caller function and then print them

"""

value = float(input("input the actual value :  "))
divisor = float(input("input the divisor  :  "))

# this  function returns the quotient and remainder ( in this order quotient , remainder )
def divide(value, divisor):
    if(divisor<1):

        print ("Please enter a valid divisor .")
        raise ValueError
    else:
        quotient = value//divisor
        remainder = value % divisor
        return quotient, remainder


try :
    quotient, remainder = divide(value, divisor)
    print(f"The quotient for this calculation is: {quotient}")
    print(f"The remainder for this calculation is: {remainder}")
except ValueError as error :
    print(error)


