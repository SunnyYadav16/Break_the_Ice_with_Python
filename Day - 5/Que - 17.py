"""
Write a program that computes the net amount of a bank account based a transaction log from console input. The
transaction log format is shown as following:

D 100
W 200
D means deposit while W means withdrawal.

Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100

Then, the output should be:
500
"""

total_amount = 0

while True:
    transaction = input().split(' ')

    if transaction[0] == 'D':
        total_amount += int(transaction[1])
    elif transaction[0] == 'W':
        total_amount -= int(transaction[1])
    else:
        break

print(total_amount)
