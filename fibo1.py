# Recursive Fibonacci
def recursive_fibonacci(n):
    if n <= 1:  # Base case
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

# Non-recursive Fibonacci (Iterative)
def non_recursive_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = a + b  # Calculate the next Fibonacci number
        a = b      # Update a to be the previous b
        b = c      # Update b to be the current c
    return b  # Return the nth Fibonacci number

# Function to test both methods
def fibonacci_comparison(n):
    print(f"Fibonacci of {n} (Recursive):", recursive_fibonacci(n))
    print(f"Fibonacci of {n} (Non-recursive):", non_recursive_fibonacci(n))

# Get user input
n = int(input("Enter a number to calculate Fibonacci: "))

# Call the comparison function
fibonacci_comparison(n)
