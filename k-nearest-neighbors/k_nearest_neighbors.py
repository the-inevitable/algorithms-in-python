"""
Suppose you run a small bakery in Berkeley, and you make fresh bread every day.
You’re trying to predict how many loaves to make for today.

You have a set of features:
• Weather on a scale of 1 to 5 (1 = bad, 5 = great).
• Weekend or holiday? (1 if it’s a weekend or a holiday, 0 otherwise.)
• Is there a game on? (1 if yes, 0 if no.)

And you know how many loaves of bread you’ve sold in the past for different sets of features.
A. (5, 1, 0) = 300
B. (3, 1, 1) = 225
C. (1, 1, 0) = 75
D. (4, 0, 1) = 200
E. (4, 0, 0) = 150
F. (2, 0, 0) = 50

Today is a weekend day with good weather. Based on the data you just
saw, how many loaves will you sell? Let’s use KNN, where K = 4.
"""

import math

# First, figure out the four nearest neighbors for this point.
# (4, 1, 0)

# Test data.
pointA = (5, 1, 0)
pointB = (3, 1, 1)
pointC = (1, 1, 0)
pointD = (4, 0, 1)
pointE = (4, 0, 0)
pointF = (2, 0, 0)

target_point = (4, 1, 0)

points_dict = {
    'A': {'point': pointA, 'amount': 300},
    'B': {'point': pointB, 'amount': 225},
    'C': {'point': pointC, 'amount': 75},
    'D': {'point': pointD, 'amount': 200},
    'E': {'point': pointE, 'amount': 150},
    'F': {'point': pointF, 'amount': 50}
}


def pythagorian_distance(p1, p2):
    """
    p1, p2 - tuples with integers.
    returns float as distance between the two points (p1, p2).
    """
    assert len(p1) == len(p2) and len(p1) > 0
    return round(math.sqrt(sum((math.pow(a - b, 2) for (a, b) in zip(p1, p2)))), 2)


def pythagorian_distance_for_multiple_points(points, target):
    """
    points - list of tuples with integers.
    returns list of distances between target and each point in points list.
    """
    return {p: pythagorian_distance(points[p]['point'], target) for p in points}


def knn(distances, k):
    sorted_distances = sorted([v for v in distances.values()])
    k_distances = sorted_distances[:k]
    return [key for key in distances if distances[key] in k_distances]


def regression(k_nearest_points, all_points):
    k_nearest_neighbors_values = [all_points[key]['amount'] for key in all_points if key in k_nearest_points]
    return sum(k_nearest_neighbors_values) / len(k_nearest_neighbors_values)


def predict_amount(points, target, k):
    distances_to_target_point = pythagorian_distance_for_multiple_points(points, target)
    k_nearest_neighbors = knn(distances_to_target_point, k)
    return regression(k_nearest_neighbors, points)


if __name__ == '__main__':
    print(predict_amount(points_dict, target_point, 4))  # 218.75
