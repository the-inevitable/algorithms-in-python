"""
Divide and Conquer strategy.
"""


def gcd(a, b):
    """
    This function returns the greatest common divisor for two integers.
    Provided integers might as well be negative.
    """
    a, b = map(abs, (a, b))
    # Base case.
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        # Recursive case.
        larger, smaller = (a, b) if a > b else (b, a)
        larger, smaller = smaller, larger % smaller
        return gcd(larger, smaller)


# Test GCD.
print(gcd(640, -1680))  # 80
