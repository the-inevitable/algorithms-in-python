"""
Divide and Conquer strategy.
"""


def recursive_lst_length(lst):
    # Base case.
    if not lst:
        return 0
    else:
        # Recursive case.
        return 1 + recursive_lst_length(lst[1:])


# Test data.
test_lst = [20, 27, 74, 76, 10, 81, 21, 85, 46, 60, 78, 43]

# Test recursive_lst_length.
print(recursive_lst_length(test_lst))
