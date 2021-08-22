"""
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example: If the following n is given as input to the program:
7

Then, the output of the program should be:
0,1,1,2,3,5,8,13
"""


class Solution:

    def func(self, n):
        n1, n2, n3 = 0, 1, 0
        if n <= 1:
            return n

        else:
            print(n1)
            print(n2)
            for i in range(2, n+1):
                n3 = n1 + n2
                n1 = n2
                n2 = n3
                print(n3)


solution = Solution()
solution.func(int(input()))
