import math

a = int(input("  Enter Coefficient a : "))
b = int(input(" Enter Coefficient b : "))
c = int(input(" Enter Coefficient c : "))

def find_roots ( a,b,c):

    disc = b**2 - 4*a*c
    if(disc>0):
        root1 = (-b+math.sqrt(disc))/(2*a)
        root2 = (-b-math.sqrt(disc))/(2*a)

        print("Roots are real and different.")
        print(f"Root 1 is : {root1}")
        print(f"Root 2 is : {root2}")
    elif disc ==0 :
        root = -b / (2 * a)
        print("Roots are real and same.")
        print(f"Root : {root}")
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(-disc) / (2*a)
        print("Roots are complex and different.")
        print("Root 1 =", real_part, "+", imag_part, "i")
        print("Root 2 =", real_part, "-", imag_part, "i")

find_roots(a,b,c)