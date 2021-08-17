"""
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise
print "No".
"""

text = input()

if text == 'yes' or text == 'YES' or text == 'YES':
    print("Yes")
else:
    print("No")