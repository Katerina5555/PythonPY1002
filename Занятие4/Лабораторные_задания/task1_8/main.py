def func_8(lst):
    return [i ** 3 if i >= 0 else 0 for i in lst]  # TODO


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(func_8(list_))