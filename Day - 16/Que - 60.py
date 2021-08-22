"""
Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=0
with a given n input by console (n>0).

Example: If the following n is given as input to the program:
5

Then, the output of the program should be:
500
"""


class Solution:

    def func(self, n):
        if n == 0:
            return 0

        return self.func(n-1) + 100


solution = Solution()
answer = solution.func(int(input()))
print(answer)


