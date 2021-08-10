"""
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print all strings line by line.
"""

class Solution:
    def convert(self, n1, n2):
        length_n1 = len(n1)
        length_n2 = len(n2)
        if length_n1 > length_n2:
            return n1
        elif length_n1 < length_n2:
            return n2
        else:
            return n1 + "\n" +n2

solution = Solution()
answer = solution.convert("Good", "Mor!")
print(answer)
print(type(answer))