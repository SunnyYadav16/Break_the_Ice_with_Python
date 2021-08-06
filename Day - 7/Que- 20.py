"""
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Suppose the following input is supplied to the program:
14

Then, the output should be:
0
7

"""

class My_class:
    def my_gen(self, n):
        for value in range(n):
            if value % 7 == 0:
                yield value


obj = My_class()
gen = obj.my_gen(int(input("Enter number: ")))

for values in gen:
    print(values)
