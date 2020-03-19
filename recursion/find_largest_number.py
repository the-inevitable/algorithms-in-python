"""
Divide and Conquer strategy.
"""


# Simple search
def find_largest_number_in_a_list(lst):
    largest = lst[0]
    for (idx, item) in enumerate(lst[1:], 1):
        if largest < (new_largest := lst[idx]):
            largest = new_largest
    return largest


# Recursive approach
def find_largest_number_recursively(lst):
    # Base case.
    if not (len_lst := len(lst)):
        return None
    elif len_lst == 1:
        return lst[0]
    elif len_lst == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    else:
        # Recursive case.
        return lst[0] if lst[0] > (rec_largest := find_largest_number_recursively(lst[1:])) else rec_largest


# Test data.
test_lst = [20, 27, 74, 76, 10, 81, 21, -85, 46, 60, 78, 43]

# Test find_largest_number_in_a_list.
print(find_largest_number_in_a_list(test_lst))    # 81

# Test find_largest_number_recursively.
print(find_largest_number_recursively(test_lst))  # 81
