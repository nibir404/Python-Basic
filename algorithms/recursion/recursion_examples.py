# Recursion Examples in Python
# Includes: Recursive Sum, Factorial, and Fibonacci

# --- 1. Recursive Sum of first 'n' natural numbers ---
# Time Complexity: O(n)
# Space Complexity: O(n) (due to call stack)
def calculate_recursive_sum(n):
    """Calculates the sum of first n numbers recursively."""
    if n <= 1:
        return n
    return n + calculate_recursive_sum(n - 1)

# --- 2. Recursive Factorial of 'n' ---
# Time Complexity: O(n)
# Space Complexity: O(n)
def calculate_factorial(n):
    """Calculates n factorial recursively."""
    if n <= 1:
        return 1
    return n * calculate_factorial(n - 1)

# --- 3. Recursive Fibonacci ---
# Time Complexity: O(2^n)
# Space Complexity: O(n)
def get_fibonacci_recursive(n):
    """Calculates the nth Fibonacci number."""
    if n <= 1:
        return n
    return get_fibonacci_recursive(n - 1) + get_fibonacci_recursive(n - 2)

# --- Main Program Execution ---
if __name__ == "__main__":
    n_sum = 5
    print(f"Sum of first {n_sum} numbers is: {calculate_recursive_sum(n_sum)}")
    
    n_fact = 5
    print(f"Factorial of {n_fact} is: {calculate_factorial(n_fact)}")
    
    n_fib = 10
    print(f"The {n_fib}th term of Fibonacci is: {get_fibonacci_recursive(n_fib - 1)}")