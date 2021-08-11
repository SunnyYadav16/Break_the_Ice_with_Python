"""
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print the first 5 elements in the list.
"""


class Solution:
    def printDict(self):
        lst = [i ** 2 for i in range(1, 21)]
        return lst[:5]


solution = Solution()
answer = solution.printDict()
print(answer)
