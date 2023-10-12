
current_unit = int(input("Enter the current unit : "))
def calculate_cost( current_unit):
    bill = 0
    remaining_unit = current_unit
    if(remaining_unit> 50):
        bill =bill+ (50*0.50)
        remaining_unit=remaining_unit-50
    if remaining_unit < 100:
        bill = bill + remaining_unit*.75
        return
    if remaining_unit>100 :
        bill = bill + (100*.75)
        remaining_unit= remaining_unit-100
    if(remaining_unit>100):
        bill = bill + remaining_unit*1.20
    if(remaining_unit>0):
        bill = bill + remaining_unit*1.50

    return bill


bill = calculate_cost(current_unit)
print(bill)

