"""
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""


def divide():
    return 5 / 0


try:
    answer = divide()
    print(answer)

except ZeroDivisionError as ze:
    print("Error - The number is getting divided by zero !!!")
