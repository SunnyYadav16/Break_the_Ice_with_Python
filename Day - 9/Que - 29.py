"""
Define a function that can accept two strings as input and concatenate them and then print it in console.
"""

class Solution:
    def convert(self, n1, n2):
        return n1 + " " +  n2

solution = Solution()
answer = solution.convert("Good", "Morning!")
print(answer)
print(type(answer))