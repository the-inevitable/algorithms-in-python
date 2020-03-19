"""
For any list of n, binary search will take log 2 n steps to run in the worst case,
whereas simple search will take n steps.

number of steps to find an element in a sorted list of n elements would be:
2**steps >= n

E.g. for a list of 1000 elements it would take no more than 10 steps.
2**10 = 1024 and 1024 > 1000 is True

O(log n) complexity
"""


def binary_search(sorted_list, item):
    low, high = 0, len(sorted_list) - 1
    attempts = 0

    while low <= high:
        attempts += 1

        mid = (low + high) // 2

        if (guess := sorted_list[mid]) == item:
            print(f'Found item << {item} >> at index {mid}. It took {attempts} attempts.')
            return mid
        elif guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        else:
            return None


# Test data.
test_list_int = list(range(200, 1232381))
test_list_str = ['Brian', 'Joe', 'Lois', 'Meg', 'Peter', 'Stevie']

# Testing the algorithm.
binary_search(test_list_int, 9999)
# Found item << 9999 >> at index 9799. It took 19 attempts.

binary_search(test_list_str, 'Stevie')
# Found item << Stevie >> at index 5. It took 3 attempts.
