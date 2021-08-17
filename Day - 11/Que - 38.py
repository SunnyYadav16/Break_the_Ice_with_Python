"""
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last
half values in one line.
"""

class Solution:

    def printtuple(self, n):
        length_n = len(n)
        print(n[:length_n//2],"\n",n[length_n//2:])

solution = Solution()
n = (1,2,3,4,5,6,7,8,9,10)
answer = solution.printtuple(n)