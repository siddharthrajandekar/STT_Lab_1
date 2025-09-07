"""
Module to compute Fibonacci numbers.

This script provides a function to compute the nth Fibonacci number
and a simple CLI interface to test it.
"""

def fibonacci(n):
    """
    Compute the nth Fibonacci number.

    Args:
        n (int): The position in the Fibonacci sequence (n >= 1).

    Returns:
        int: The nth Fibonacci number, or -1 if n <= 0.
    """
    if n <= 0:
        return -1
    if n in (1, 2):
        return 1

    first, second = 1, 1
    ans = 0
    for _ in range(n - 2):
        ans = first + second
        first, second = ans, first

    return ans


def main():
    """
    Read user input and print the nth Fibonacci number.
    """
    n = int(input("Enter an integer: "))
    fibo = fibonacci(n)
    if fibo == -1:
        print("The integer should be greater than 0")
    else:
        print(fibo)


if __name__ == "__main__":
    main()
