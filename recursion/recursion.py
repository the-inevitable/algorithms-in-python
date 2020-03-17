"""
Dividing big problem into smaller tasks and using recursion to solve the problem.

Every recursive algorithm must have at least one base case and a recursive case.
"""


def factorial(n):
    """
    Factorial of n (n!) = n * (n-1) * (n-2) * ... 2 * 1
    """
    # Base cases.
    if n < 0 or not isinstance(n, int):
        print(f'Arguments must be positive integers. But {n} received.')
        return
    elif n in [0, 1]:
        return 1
    # Recursive case.
    else:
        return n * factorial(n - 1)


# Test recursive factorial.
print(factorial(10))  # 3628800


def fibonacci(n):
    """
    Fibonacci sequence is a sequence, where  each number is the sum of the two preceding ones.
    E.g. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...
    """
    if n < 0 or not isinstance(n, int):
        print(f'Arguments must be positive integers. But {n} received.')
        return
    elif n in [0, 1]:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Test recursive fibonacci.
fibonacci_sequence = [fibonacci(i) for i in range(15)]
print(fibonacci_sequence)  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
