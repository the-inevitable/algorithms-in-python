"""
For any list of n, binary search will take log 2 n steps to run in the worst case,
whereas simple search will take n steps.

number of steps to find an element in a sorted list of n elements would be:
2**steps >= n

E.g. for a list of 1000 elements it would take no more than 10 steps.
2**10 = 1024 and 1024 > 1000 is True
"""


def binary_search(sorted_list, item):
    low, high = 0, len(sorted_list) - 1
    attempts = 0

    while low <= high:
        attempts += 1

        mid = (low + high) // 2
        guess = sorted_list[mid]

        if guess == item:
            print(f'Found element at {mid} index. It took {attempts} attempts.')
            return mid
        elif guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        else:
            return None


test_list = list(range(200, 1232381))

idx = binary_search(test_list, 9999)


