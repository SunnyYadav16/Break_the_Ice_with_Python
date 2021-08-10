"""
Define a function that can receive two integer numbers in string form and compute their sum and then print it in
console.
"""

class Solution:
    def convert(self, n1, n2):
        return int(n1) + int(n2)

solution = Solution()
answer = solution.convert("1", "2")
print(answer)
print(type(answer))