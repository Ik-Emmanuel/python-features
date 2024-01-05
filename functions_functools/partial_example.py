from functools import partial

"""
partials preload functions and readies them to be called later
"""

def add_numbers(num:int, second_num: int) -> int:
    return num + second_num

my_list = [1,2,3,4]
for i in my_list:
    new_func = partial(add_numbers, second_num=i)
    value = new_func(6)
    print(value)