n = int(input("Enter the factorial number : "))
factorial = 1
for i in range(1, n + 1):
    previous_factorial = factorial
    factorial = i * factorial
    print(f"In {i} iteration factorial is {previous_factorial} X {i} = {factorial}")
print(f"Factorial of {n} is = {factorial}")
