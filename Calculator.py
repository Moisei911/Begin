f_number = float(input("first number:"))

operation = input("operation:")
# operation

s_number = float(input("second number:"))

if operation == "+":
    print(f_number + s_number)

elif operation == "-":
    print(f_number - s_number)

elif operation == "/":
    print(f_number / s_number)

elif operation == "*":
    print(f_number * s_number)

else:
    print("incorrect operation")
input()