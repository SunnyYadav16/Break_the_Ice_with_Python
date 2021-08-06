"""
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2

The numbers after the direction are steps. Please write a program to compute the distance from current position after a
sequence of movement and original point. If the distance is a float, then just print the nearest integer.

Example: If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2

Then, the output of the program should be:
2
"""

import math

x_axis = 0
y_axis = 0

lst = []
while True:
    movements = input().split(" ")
    if not movements[0]:
        break
    lst.append(tuple(movements))

for direction in lst:
    if direction[0] == "UP":
        y_axis += int(direction[1])

    elif direction[0] == "DOWN":
        y_axis -= int(direction[1])

    elif direction[0] == "RIGHT":
        x_axis += int(direction[1])

    else:
        x_axis -= int(direction[1])


distance = round(math.sqrt(x_axis ** 2 + y_axis ** 2))
print(distance)
