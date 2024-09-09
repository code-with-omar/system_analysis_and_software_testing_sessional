def calculation(number1, operator, number2):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return int(number2 / number2)


with open("input.txt", "r") as file:
    input_data = file.read()
print(input_data)

elements = list(map(int, input_data.replace(",", " ").split()))
print(elements)
n = len(elements)
for i in range(0, n, 2):
    addition = calculation(elements[i], "+", elements[i + 1])
    subtraction = calculation(elements[i], "-", elements[i + 1])
    multiplication = calculation(elements[i], "*", elements[i + 1])
    division = calculation(elements[i], "/", elements[i + 1])
    result = [addition, subtraction, multiplication, division]
    with open("output.txt", "a") as file:
        file.write(f"Case {i//2+1} : " + " ".join(map(str, result)) + "\n")
