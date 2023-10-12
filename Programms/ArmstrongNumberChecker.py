number_str = input("Enter the number : ")

def check_armstrong_number (num_str):
    numlength = int(len (num_str))

    sum = 0
    for i in num_str:
        digit = int(i)
        sum = sum+ pow(digit,numlength)

    if(sum == int(num_str)):
        print("This number is a armstrong number ")
    else:
        print("This number is not a armstrong number")


check_armstrong_number(number_str)
