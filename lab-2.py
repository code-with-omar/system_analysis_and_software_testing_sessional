def calculation(number1, operator, number2):
    if operator == "+":
        return number1 + number2

    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    elif operator == "%":
        return number1 % number2
    else:
        print("Please Enter Valid Operator (+, -, *, /, % )")


n = int(input("Please Enter n: "))
elements = input(
    f"Please Enter {n*2} Element space by space and at last please enter a operator(+,-,*,/,%) : "
).split(" ")
operator = elements[-1]
print(operator)
elements = list(map(int, elements[:-1]))
print(elements)
for i in range(0, 2 * n, 2):
    cal = calculation(elements[i], operator, elements[i + 1])
    print(cal, end=" ")
print()