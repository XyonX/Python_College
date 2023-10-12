

# Arithmetic operations


number1 = int(input("Type Number 1 :"))
number2 = int(input("Type Number 2 :"))

def Arithmetic_operations ( num1, num2) :

    if num2 == 0:
        print("divisor is zero division is not possible")

    else:
        return num1 + num2,num1 - num2,num1 * num2,num1/num2


addition, subtraction, multiplication, division = Arithmetic_operations(number1, number2)

#print (" the addition value is : {}",addition)
#print (" the subtraction vale is : {} ", subtraction)
#print (" the mutiplication value is : {} ", multiplication)
#print (" the division value is : {}" , division)

print ("The addition value is : {}".format(addition))
print ("The subtraction value is : {}".format(subtraction))
print ("The multiplication value is : {}".format(multiplication))
print ("The division value is : {}".format(division))

