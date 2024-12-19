def calculate_electricity_bill(units):
    if units <= 100:
        cost = 0
    elif 200 >= units > 100 :
        cost = 0 + (units-100)*5
    else:
        cost = 500 + (units-200)*10
    return cost
units = int(input())
print(calculate_electricity_bill(units))