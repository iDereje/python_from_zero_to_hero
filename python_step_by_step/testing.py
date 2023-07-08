first_number = float(input("please enter a number"))
second_number = float(input("please enter another number"))
sign = input("please choose calculation sign (+/-/*/\)")
add = first_number + second_number
subtract = first_number - second_number
multiply = first_number * second_number
divide = first_number / second_number

if sign == "+":
    print(add)
elif sign == "-":
    print(subtract)
elif sign == "*":
    print(multiply)
else:
    print(divide)
