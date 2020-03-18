"""
Divide and Conquer strategy.
"""


def recursive_sum(lst):
    # Base case.
    if not lst:
        return 0
    else:
        # Recursive case.
        return lst[0] + recursive_sum(lst[1:])


# Test recursive sum.
print(recursive_sum([1, 2, 3, 8, 5, 13]))  # 32
