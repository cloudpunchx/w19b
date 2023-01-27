import helpers.addition as add
import helpers.subtraction as subtract
import helpers.multiplication as multiply
import helpers.division as divide

print("Welcome to the simple calculator, please select from the following options:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
selection = input("Please enter your selection: ")
selection = int(selection)
if (selection == 1):
    x = input("Type first number: ")
    y = input("Type second number: ")
    x_num = int(x)
    y_num = int(y)
    add.add(x_num, y_num)
elif (selection == 2):
    x = input("Type first number: ")
    y = input("Type second number: ")
    x_num = int(x)
    y_num = int(y)
    subtract.subtract(x_num, y_num)
elif (selection == 3):
    x = input("Type first number: ")
    y = input("Type second number: ")
    x_num = int(x)
    y_num = int(y)
    multiply.multiply(x_num, y_num)
elif (selection == 4):
    x = input("Type first number: ")
    y = input("Type second number: ")
    x_num = int(x)
    y_num = int(y)
    divide.divide(x_num, y_num)
else:
    print("Please make a selection from 1-4")
