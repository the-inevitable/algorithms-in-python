"""
Divide and Conquer strategy.
"""
import random


def quicksort(lst):
    # Base case.
    if len(lst) < 2:
        return lst
    elif len(lst) == 2:
        return lst if lst[0] < lst[1] else [lst[1], lst[0]]
    else:
        # Recursive case.

        # Pick a pivot.
        pivot = random.choice(lst)

        # Partition the list.
        smaller_lst = [x for x in lst if x < pivot]
        larger_lst = [x for x in lst if x > pivot]

        # Call quicksort recursively on each of the lists.
        # They will eventually reach the base case.
        # Return concatenated lists.
        return quicksort(smaller_lst) + [pivot] + quicksort(larger_lst)


# Test data.
test_lst = [16, 62, 65, 86, 23]
test_lst1 = [15, 71, 70, 59, 37, 28, 96, 48, 76, 20, 60, 8, 38, 31, 25]
test_lst2 = [
    101, 904, 76, 930, 514, 842, 35, 564, 104, 153,
    967, 464, 113, 943, 219, 660, 739, 393, 503, 804,
    451, 31, 876, 507, 556, 808, 28, 349, 197, 318,
    398, 285, 441, 572, 533, 635, 183, 782, 766, 82,
    67, 785, 976, 288, 846, 819, 916, 855, 732, 649,
    184, 770, 238, 990, 296, 37, 671, 448, 877, 79,
    457, 419, 43, 957, 616, 245, 911, 174, 843, 608,
    85, 688, 580, 475, 644, 364, 868, 650, 940, 409,
    225, 838, 679, 578, 453, 53, 462, 717, 494, 178,
    826, 726, 969, 254, 984, 430, 282, 363, 648, 542
]

# Test quicksort.
print(quicksort(test_lst))   # [16, 23, 62, 65, 86]
print(quicksort(test_lst1))  # [8, 15, 20, 25, 28, 31, 37, 38, 48, 59, 60, 70, 71, 76, 96]
print(quicksort(test_lst2))
# [
#     28, 31, 35, 37, 43, 53, 67, 76, 79, 82,
#     85, 101, 104, 113, 153, 174, 178, 183, 184, 197,
#     219, 225, 238, 245, 254, 282, 285, 288, 296, 318,
#     349, 363, 364, 393, 398, 409, 419, 430, 441, 448,
#     451, 453, 457, 462, 464, 475, 494, 503, 507, 514,
#     533, 542, 556, 564, 572, 578, 580, 608, 616, 635,
#     644, 648, 649, 650, 660, 671, 679, 688, 717, 726,
#     732, 739, 766, 770, 782, 785, 804, 808, 819, 826,
#     838, 842, 843, 846, 855, 868, 876, 877, 904, 911,
#     916, 930, 940, 943, 957, 967, 969, 976, 984, 990
# ]
