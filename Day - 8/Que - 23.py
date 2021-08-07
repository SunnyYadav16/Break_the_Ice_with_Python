"""
Write a method which can calculate square value of number
"""

class Solution:

    def find_square(self, number):
        square_value = number ** 2
        return square_value


solution = Solution()
answer = solution.find_square(int(input("Enter a number: ")))
print(answer)