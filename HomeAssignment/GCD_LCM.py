

number1 = int(input(" Enter the number 1 : "))
number2 = int(input(" Enter the number 2 : "))

def calculate_gcd (num1 , num2 ):

    if(num1<num2):
        loop_count = num1
    else:
        loop_count = num2
    gcd = 1

    for i in range(2, loop_count + 1):
        if num1 % i == 0:
            if (num2 % i == 0):
                gcd = i
    return gcd

def calculate_LCM (num1 , num2 ):

    if(num1>num2):
        startcount = num1
    else:
        startcount = num2

    lcm = 1
    shouldbreak = False
    count =startcount ;
    while ( shouldbreak  == False ):
        if count%num1 == 0:
            if (count%num2 == 0):
                lcm=count
                shouldbreak = True
        count = count +1

    return lcm


gcd = calculate_gcd(number1,number2)

lcm = calculate_LCM(number1,number2)
print (" the gcd of  this number is : {}".format(gcd))
print(f" the lcm of  this number is : {lcm}")