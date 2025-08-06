# a simple calculator program

# ask the user for the first number


num1 = input("Enter the first number:")
num1 = float(num1) # converts the input into a number

# ask the user for the second number

num2 = input("Enter the second number:")
num2 = float(num2) # converts the input into a number

# ask the user which operation to perfom
print("Choose an operation: + for addition, - for subtraction, * for multiplication, / for division")
operation = input("Enter the operation")

# to perfom the right calculation

if operation:
    result = num1 + num2
    print("The result is: " + str(result))

elif operation == "-":
    result = num1 - num2
    print("The result is: " + str(result))

elif operation == "*":
    result = num1 * num2
    print("The result is: " + str(result))


elif operation == "/":
    if num2 != 0:
       result = num1 / num2
       print("The result is: " + str(result))

    else:   
        print("Sorry! Zero can't be divided")
        
else:
    print("The operation is invalid. Please choose +,-,*,or /.")


