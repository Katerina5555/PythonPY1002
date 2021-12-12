import random
def fun_2(lst):
    print(lst)
    return len([i for i in lst if i > lst[0]])

if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list1 = [random.randint(-10, 10) for _ in range(20)]
    print(fun_2(list_))
    print(fun_2(list1))
