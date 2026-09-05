print("SMART EXPENSE SPLITTER")

name = input ("What is your name?")
print("Hello",name)

income = float(input("What is your income"))
print(income)

food = float(input("How much do you spend on food? "))
transport = float(input("How much you spend on transport?"))
internet = float(input("how much is your internet bills?"))
other = float(input("other expenses?"))

total_expense = food + transport + internet + other
remaning = income - total_expense

savings_rate = (remaning / income)* 100

print("\n===== YOUR RESULT =====")
print("Name:", name)
print("Monthly income:", income)
print("Total expenses:", total_expense)
print("Money remaining:", remaning)
print("Savings rate:", savings_rate, "%")