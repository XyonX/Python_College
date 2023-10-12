number = int(input("Enter the number : "))

def find_factorial(num):
    result = 1
    for i in range ( 1,num+1):
        print(i)
        result =result*i
    return result

res=find_factorial(number)
print(res)