"""
O(n**2) sorting algorithm.
Each time we iterate through the list, we select the smallest / largest item and put it in another list.
Then repeat this procedure while continuing appending found item to the list.

So we go through N elements of a list N times. To be precise, it's 1/2 * N, but we ignore 1/2 in Big O Notation.
"""


def find_smallest(lst):
    # Store smallest number and its index.
    smallest = lst[0]
    smallest_idx = 0

    # Iterating through the rest of the list.
    for (idx, elem) in enumerate(lst[1:], 1):
        if elem < smallest:
            smallest = elem
            smallest_idx = idx
    return smallest_idx


def selection_sort(lst):
    sorted_list = []
    for _ in range(len(lst)):
        smallest_idx = find_smallest(lst)
        sorted_list.append(lst[smallest_idx])
        del lst[smallest_idx]
    return sorted_list


# Test data.
test_data = [15, 58, 73, 27, 7, 50, 43, 28, 57, 85]
test_data1 = [101, 904, 76, 930, 514, 842, 35, 564, 104, 153,
      967, 464, 113, 943, 219, 660, 739, 393, 503, 804,
      451, 31, 876, 507, 556, 808, 28, 349, 197, 318,
      398, 285, 441, 572, 533, 635, 183, 782, 766, 82,
      67, 785, 976, 288, 846, 819, 916, 855, 732, 649,
      184, 770, 238, 990, 296, 37, 671, 448, 877, 79,
      457, 419, 43, 957, 616, 245, 911, 174, 843, 608,
      85, 688, 580, 475, 644, 364, 868, 650, 940, 409,
      225, 838, 679, 578, 453, 53, 462, 717, 494, 178,
      826, 726, 969, 254, 984, 430, 282, 363, 648, 542]

# Testing selection sort algorithm.
new_lst = selection_sort(test_data)
print(new_lst)
# [7, 15, 27, 28, 43, 50, 57, 58, 73, 85]

new_lst1 = selection_sort(test_data1)
print(new_lst1)
# [28, 31, 35, 37, 43, 53, 67, 76, 79, 82,
# 85, 101, 104, 113, 153, 174, 178, 183, 184,
# 197, 219, 225, 238, 245, 254, 282, 285, 288,
# 296, 318, 349, 363, 364, 393, 398, 409, 419,
# 430, 441, 448, 451, 453, 457, 462, 464, 475,
# 494, 503, 507, 514, 533, 542, 556, 564, 572,
# 578, 580, 608, 616, 635, 644, 648, 649, 650,
# 660, 671, 679, 688, 717, 726, 732, 739, 766,
# 770, 782, 785, 804, 808, 819, 826, 838, 842,
# 843, 846, 855, 868, 876, 877, 904, 911, 916,
# 930, 940, 943, 957, 967, 969, 976, 984, 990]

print(new_lst[0] == min(new_lst) and new_lst[-1] == max(new_lst))      # True
print(new_lst1[0] == min(new_lst1) and new_lst1[-1] == max(new_lst1))  # True
