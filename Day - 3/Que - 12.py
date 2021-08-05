"""
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

# Approach I
out_list = [str(i) for i in range(1000,3001)]

out_list = list(filter(lambda i: all(ord(j) % 2 == 0 for j in i),out_list))

print(*out_list)


# Approach II
for i in range(1000,3001):
    s = str(i)
    if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0 and int(s[3]) % 2 == 0:
        out_list.append(i)

print(*out_list)