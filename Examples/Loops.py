

looplength = 10
my_list = [10,20,30,30,"AnyString"]
my_tuple = (10,20,30,30,"AnyString")
my_sets = {10,20,30,30}

for i in my_list:
    print(type(i))
    print(i)

for i in my_sets:
    print(type(i))
    print(i)

# in Python the for loop exppects a iteratable object
for i in range (looplength):
    print(i)