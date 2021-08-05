"""
Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated
sequence on a single line.
Suppose the following input is supplied to the program: 8
Then, the output should be:40320.
"""

# Approach I
def fact(n):
    if n < 0:
        return "Enter +ve integer"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)


if __name__ == '__main__':
    number = int(input())
    answer = fact(number)
    print(answer)




# Approach II
number = int(input())
fact = 1
i = 1
while i <= number:
    fact = fact * i
    i += 1

print(fact)
