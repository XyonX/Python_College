

number1 = float(input(" type number 1 : "))
number2 = float(input(" type number 2 : "))

def check_the_largest_number(num1, num2):
    if num1>num2:
        return num1
    else:
        return num2


largest_number = check_the_largest_number(number1, number2)

print ( " the largest nnmber is : {}".format(largest_number))

