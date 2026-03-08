# Fibonacci Sequence implementation in Python
# Includes both Iterative and Recursive versions
# Time Complexity (Recursive): O(2^n)
# Time Complexity (Iterative): O(n)
# Space Complexity (Iterative): O(1)

# --- 1. Iterative Fibonacci ---
def print_fibonacci_iterative(num_count):
    """Prints Fibonacci sequence using an iterative loop."""
    first_num = 0
    second_num = 1
    
    print(f"Iterative ({num_count} terms):", end=" ")
    for _ in range(num_count):
        print(first_num, end=" ")
        # Updating the values
        first_num, second_num = second_num, first_num + second_num
    print()

# --- 2. Recursive Fibonacci ---
def get_fibonacci_recursive(n):
    """Calculates the nth Fibonacci number using recursion."""
    if n <= 1:
        return n
    else:
        return get_fibonacci_recursive(n-1) + get_fibonacci_recursive(n-2)

# --- Main Program ---
if __name__ == "__main__":
    count = int(input("Enter the number of terms for Fibonacci sequence: "))
    
    # Run the iterative version
    print_fibonacci_iterative(count)
    
    # Run the recursive version and print the nth term
    print(f"Recursive: The {count}th term is {get_fibonacci_recursive(count-1)}")