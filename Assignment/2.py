"""
How memory location of a variable can be printed? If value of the variable
is reassigned, how it effects the memory location?
"""

# The memory location of a variable can be printed by using the id functioin

#Assigning first value
testVar = 10
print(f"The location of the variable {testVar} is { id(testVar)}")  #Output: The location of the variable 10 is 140718230725704



#Assignign a new value to the testVar
testVar = 20
print(f"The location of the variable {testVar} is { id(testVar)}") #Output: The location of the variable 20 is 140718230726024


newVar = 20
print(f"The location of the variable {newVar} is { id(newVar)}") #Output: The location of the variable 20 is 140718230726024

"""
    Conclusion : Changing A value of a particular variable changes its Memory location 
    
    If two different variable has same value it should have the same memory address(Mostly , But Not Always  )
    
    So the memory allocation is done based on the value not tied to a specific variable 
"""


#Question
"""
whats about used defined data types object for example a instance of a class if two variable differently creates two object of the class 
and they fills the exact number of variable and exact same value to those will they share same memory address

"""
