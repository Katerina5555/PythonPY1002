# if __name__ == "__main__":
#     i = 15
#     length = len(str(i**2)) + 3
#     width = len(str(i)) +3
#
#     headers = " " * width + " " + "".join([str(j).rjust(length) for j in range(1, i+1)])
#     print(headers)      # или так 1
#     dashes = " " * width + ":" + "-" * length * i
#     print(dashes)      # или так 1
#
#     body = ""
#     for row in range(1, i+1):
#         body += str(row).rjust(width) + ":"
#         for column in range(1, i+1):
#             body += str(row * column).rjust(length)
#         body += "\n"
#
#     print(body)     # или так 1
#     print("\n".join([headers, dashes, body]))       # или так 2


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3, 4]))

# def change(lst: list):
#     new_first = lst.pop()
#     new_end = lst.pop(0)
#     lst.append(new_end)
#     lst.insert(0, new_first)
#     return lst
#
# print(change([1, 2, 3, 4]))

# def to_list(*args):
#     return list(args)
#
# print(to_list(1, 2, 3))
# print(to_list('1', '2', '3'))
# print(to_list([1, 2, 3], ['1', '2', '3']))
#
# def to_list(**kwargs):   #аргументы ключ-значение
#     return kwargs
#
# print(to_list(a=1, b=2, c=3))
# print(to_list(some_a = '1', some_b = '2', some_z ='3'))
# print(to_list(cat = [1, 2, 3], dog = ['1', '2', '3']))

# def list_sort(lst):
#     lst.sort(key=abs, revers=True)
#     return lst
#
# print(list_sort([1, -4, 0]))


import random

# def all_eq(lst):
#     a = len(max(lst, key=len))
#     lst.ljust(a, "-")
#     return lst
#
# print(all_eq('''1234567
# 123
# 1132213'''))

# def all_eq1(lst):
#     max_elem = len(max(lst, key=len))
#     return [elem.ljust(max_elem, '_') for elem in lst]
#
# lst = ['1', '123', '23424']
# print(all_eq1(lst))

# def to_dict(lst):
#     return {elem:elem+10 for elem in lst}
#
# lst = [1, 123, 23424]
# print(to_dict(lst))

import random
def count_it(str_: str):
    def sort_rule(x):
        return x[1]
    n_dict = {int(item): str_.count(item) for item in str_}
    print(n_dict.items())
    sort_ = sorted(n_dict.items(), key=sort_rule)[-3:]
    print(sort_)
    return dict(sort_)

print(count_it('82123331423343242'))
