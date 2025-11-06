# Recursive Fibonacci function
def recursive_fibonacci(n):
    if n <= 1:  # Base case
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

# Non-recursive (iterative) Fibonacci function
def non_recursive_fibonacci(n):
    sequence = []  # List to store Fibonacci numbers
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Function to generate Fibonacci sequence using recursion
def recursive_sequence(n):
    seq = []
    for i in range(n):
        seq.append(recursive_fibonacci(i))
    return seq

# Function to test and display both methods
def fibonacci_comparison(n):
    print(f"\nFibonacci sequence up to {n} terms (Recursive):")
    print(recursive_sequence(n))

    print(f"\nFibonacci sequence up to {n} terms (Non-recursive):")
    print(non_recursive_fibonacci(n))

# Get user input
n = int(input("Enter number of terms for Fibonacci sequence: "))

# Call the comparison function
fibonacci_comparison(n)
