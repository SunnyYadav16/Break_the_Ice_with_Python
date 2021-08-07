"""
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some
books. But Python has a built-in document function for every built-in functions, i.e, __doc__.

Please write a program to print some Python built-in functions documents, such as abs(), int(), input()

And add document for your own function
"""

print(str.__doc__)
print(sorted.__doc__)


def power(n, p):
    """
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    """

    return n ** p


print(power(3, 4))
print(power.__doc__)
