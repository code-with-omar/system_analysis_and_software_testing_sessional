
# Function to calculate the sum of an array
def calculate_sum(arr):
    total_sum = 0
    i = 0
    while True:
        total_sum += arr[i]
        i += 1
        if i >= len(arr):
            break
    return total_sum

# Function to calculate the average of an array
def calculate_average(arr, total_sum):
    return total_sum / len(arr)

# Main program to take input and calculate sum and average
def main():
    arr = []
    
    while True:
        n = int(input("Enter the number of elements in the array (must be at least 1): "))
        if n > 0:
            break
        print("Please enter a valid number greater than 0.")
    
    for i in range(n):
        element = float(input(f"Enter element {i+1}: "))
        arr.append(element)

    # Calculate sum using the defined function
    total_sum = calculate_sum(arr)
    print(f"Sum of the array: {total_sum}")

    # Calculate average using the defined function
    average = calculate_average(arr, total_sum)
    print(f"Average of the array: {average}")

# Run the main program
main()
