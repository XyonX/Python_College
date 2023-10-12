
number = int(input("Enter the number : "))

def prime_checker(num):

    for i in range(2, num//2+1) :
        if(num% i ==0):
            return False
        return True


res = prime_checker(number)
print(res)