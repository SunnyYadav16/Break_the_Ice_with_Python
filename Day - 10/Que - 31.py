"""
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the
values are square of keys.
"""


# APPROACH I
class Solution:
    def print_dict(self):
        my_dict = {}
        for value in range(1, 21):
            my_dict[value] = value ** 2

        return my_dict


solution = Solution()
answer = solution.print_dict()
print(answer)


# APPROACH II
def printDict():
    dict = {i: i ** 2 for i in range(1, 21)}
    print(dict)


printDict()
