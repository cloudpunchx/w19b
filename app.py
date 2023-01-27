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
# change input into integer
selection = int(selection)
# set is_valid to False so when an error happens, the calculator asks for input again
is_valid = False
# keep running script until is_valid becomes True
while not is_valid:
    if (selection == 1):
        x = input("Type first number: ")
        y = input("Type second number: ")
        try: 
            # change inputs into integers
            x_num = int(x)
            y_num = int(y)
            add.add(x_num, y_num)
            # change is_valid to True after succeeding to break the loop
            is_valid = True
        except ValueError:
            print("Invalid character entered.")
    elif (selection == 2):
        x = input("Type first number: ")
        y = input("Type second number: ")
        try: 
            x_num = int(x)
            y_num = int(y)
            subtract.subtract(x_num, y_num)
            is_valid = True
        except ValueError:
            print("Invalid character entered.")
    elif (selection == 3):
        x = input("Type first number: ")
        y = input("Type second number: ")
        try: 
            x_num = int(x)
            y_num = int(y)
            multiply.multiply(x_num, y_num)
            is_valid = True
        except ValueError:
            print("Invalid character entered.")
    elif (selection == 4):
        x = input("Type first number: ")
        y = input("Type second number: ")
        try: 
            x_num = int(x)
            y_num = int(y)
            divide.divide(x_num, y_num)
            is_valid = True
        except ValueError:
            print("Invalid character entered.")
    else:
        print("Please make a selection from 1-4")