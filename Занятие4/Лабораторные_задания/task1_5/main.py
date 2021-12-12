def fun_2(lst):
    even = len([i for i in lst if i % 2 == 0])
    odd = len([i for i in lst if i % 2 != 0])

    if even > odd:
        return "Четных больше"
    elif even < odd:
        return "Нечетных больше"
    return "Количество равно"

if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(fun_2(list_))
    print(fun_2(range(1, 10)))
    print(fun_2(range(3, 5)))
    print(fun_2([2, 2, 2, 3]))