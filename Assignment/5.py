"""

Write a class Number with
one class variable var1 ,
one private data member var2
and display( ) method
to display var1 and var2.

"""


class Number:

    def __init__(self, num1, num2):
        self.var1 = num1
        self._var2= num2

    #Declaration of a public member variable
    var1 = None
    # Declaration of a protected member variable
    _var2 =None
    #declaration of a strictly private variable
    __var3 = None

    def display(self):
        print(self.var1)
        print(self._var2)


numberObject = Number(10, 5)
numberObject.display()

#Output
"""
C:\Projects\College\Python\venv\Scripts\python.exe C:/Projects/College/Python/Assignment/5.py
10
5

"""

