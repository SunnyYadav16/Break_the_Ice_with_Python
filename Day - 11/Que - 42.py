"""
Write a program which can map() and filter() to make a list whose elements are square of even number in
[1,2,3,4,5,6,7,8,9,10].
"""

my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

final_list = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, my_lst))

print(list(final_list))
