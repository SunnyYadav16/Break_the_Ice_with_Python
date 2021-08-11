"""
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20
(both included).
"""


class Solution:
    def printDict(self):
        lst = [i ** 2 for i in range(1, 21)]
        return tuple(lst)


solution = Solution()
answer = solution.printDict()
print(answer)
