"""
Longest common substring algorithm.

Works on sequences of any lengths.

O(n)
"""


def lcs(s1, s2):
    if not len(s1) or not len(s2):
        return 0
    grid = [[0] * len(s1) for _ in s2]
    for idx, tpl in enumerate(zip(s1, s2)):
        if tpl[0] == tpl[1]:
            substracted_idx = idx - 1 if idx > 0 else idx
            grid[idx][idx] = grid[substracted_idx][substracted_idx] + 1
        else:
            grid[idx][idx] = 0
    return max(max(row) for row in grid)


# Test data.
str1 = ''
str2 = 'fishazxczasda'

str11 = 'foshfadzxczxc'
str21 = 'fortazxczasda'

str12 = 'fishfadzxczxc'
str22 = 'fistazxczasdaasdaqewegzxca'

# Test the algorithm
print(lcs(str1, str2))    # 0
print(lcs(str11, str21))  # 2
print(lcs(str12, str22))  # 3
