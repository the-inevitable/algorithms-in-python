"""
Longest common subsequence algorithm.

Works on sequences of any lengths.

O(n**2)
"""


def lcs(s1, s2):
    if not len(s1) or not len(s2):
        return 0
    max_len = max((len(s1), len(s2)))
    grid = [[0] * max_len for _ in range(max_len)]
    for i, ch1 in enumerate(s1):
        for j, ch2 in enumerate(s2):
            if ch1 == ch2:
                grid[i][j] = grid[i-1 if i > 0 else i][j-1 if j > 0 else j] + 1
            else:
                grid[i][j] = max([
                    grid[i-1 if i > 0 else i][j],
                    grid[i][j-1 if j > 0 else j]
                ])
    return max(max(row) if row else [0] for row in grid)


# Test data.
str1 = ''
str2 = ''

str11 = 'foshfadzxczxc'
str21 = 'fortazxczasda'

str12 = 'fishfadzxczxczzzzzzzzzzzzzzzzzzzzzzzzzzzz'
str22 = 'fistazxczasdaasaaaaaaaaaa'

# Test the algorithm
print(lcs(str1, str2))    # 0
print(lcs(str11, str21))  # 7
print(lcs(str12, str22))  # 8
