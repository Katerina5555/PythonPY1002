def sum_list():
    n = int(input("Введите ряд чисел:  "))
    list_ = []
    if n > 0:
        list_.append(n)
        while n != 0:
            n = int(input("Введите ряд чисел:  "))
            if n > 0:
                list_.append(n)
    else:
        print("Нет объектов для отображения")
    return sum(list_)
if __name__ == "__main__":
    print(sum_list())
pass
