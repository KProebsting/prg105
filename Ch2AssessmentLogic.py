

monthly_income = int(input("What is your total monthly income? "))
housing = int(input("How much do you spend on housing each month? "))
food = int(input("ho much do you spend on food monthly?"))
transportation = int(input("How much do you spend on transportation each month? "))
phone = int(input("How much do you spend on your phone bill each month? "))
utilities = int(input("How much do you spend on utilities each month?"))
clothing = int(input("How much do you spend on clothing each month?"))

print("Housing takes up " + format(monthly_income/housing, '.2f') + " % of your monthly income")
print("food takes up " + format(monthly_income/food, '.2f') + " % of your monthly income")
print("Transportation takes up " + format(monthly_income/food/transportation, '.2f') + " % of your monthly income")
print("Phone takes up " + format(monthly_income/phone, '.2f') + " % of your monthly income")
print("Utilities takes up " + format(monthly_income/utilities, '.2f') + " % of your monthly income")
print("Clothing takes up " + format(monthly_income/clothing, '.2f') + " % of your monthly income")
