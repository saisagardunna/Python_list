def sum_of_even_numbers(n):
    # Initialize the sum
    total_sum = 0
    
    # Iterate through all numbers from 1 to n
    for number in range(1, n + 1):
        # Check if the number is even
        if number % 2 == 0:
            total_sum += number
    
    return total_sum

# Example usage
n = int(input("Enter a positive integer: "))
print("Sum of all even numbers between 1 and", n, "is:", sum_of_even_numbers(n))
