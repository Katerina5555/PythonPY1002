def func_1(list_):
    average = sum(list_) / len(list_)
    print(average)
    return [x for x in list_ if x > average]
if __name__ == "__main__":
    print(func_1(range(1, 9)))
    print(func_1(range(3, 5)))
    print(func_1(range(4, 14)))