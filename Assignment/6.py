"""
Write a Python code to find out GCD of a number using recursion.
"""

def calculate_gcd(num1, num2 ,gcd = 1 ,first_iteration = True,max_count = None , current_count = 2):

    if first_iteration:
        gcd = 1
        if num1 < num2:
            max_count = num1
        else:
            max_count = num2

    if num1 % current_count == 0 and num2 % current_count ==0:
        gcd = current_count

    if current_count < max_count:
        return calculate_gcd(num1, num2, gcd, False, max_count, current_count + 1)
    return gcd


number1 = 24
number2 = 18
gcdd = calculate_gcd(number1,number2)
print ( f"gcd of num {number1} and {number2} is : {gcdd}")

"""
C:\Projects\College\Python\venv\Scripts\python.exe C:/Projects/College/Python/Assignment/6.py
gcd of num 24 and 18 is : 6

Process finished with exit code 0

"""