"""
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all
duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again

Then, the output should be:
again and hello makes perfect practice world
"""

# Approach I
sequence = input().split(' ')
final_sequence = []

for i in range(len(sequence)):
    if sequence[i] not in sequence[i+1:]:
        final_sequence.append(sequence[i])

final_sequence.sort()

print(*final_sequence)


# Approach II
#  input string splits -> converting into set() to store unique values
#  element -> converting into list to be able to apply sort
word = sorted(list(set(input().split())))
print(" ".join(word))

