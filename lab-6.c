#include <stdio.h>

// Function to calculate the sum of an array
int calculate_sum(int arr[], int size) {
    int sum = 0, i = 0;
    do {
        sum += arr[i];
        i++;
    } while (i < size);
    return sum;
}

// Function to calculate the average of an array
float calculate_average(int sum, int size) {
    return (float)sum / size;
}

// Main function to take input and calculate sum and average
int main() {
    int n;

    // Input number of elements in the array
    do {
        printf("Enter the number of elements in the array (must be at least 1): ");
        scanf("%d", &n);
    } while (n <= 0);  // Ensures user enters a positive number

    int arr[n];

    // Input array elements
    for (int i = 0; i < n; i++) {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    // Calculate sum using the user-defined function
    int sum = calculate_sum(arr, n);
    printf("Sum of the array: %d\n", sum);

    // Calculate average using the user-defined function
    float average = calculate_average(sum, n);
    printf("Average of the array: %.2f\n", average);

    return 0;
}
