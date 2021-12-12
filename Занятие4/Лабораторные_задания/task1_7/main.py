def func_7(list_):
    average = sum(list_) / len(list_)
    print(average)
    return [round(x - average, 1) for x in list_]

if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(func_7(list_))