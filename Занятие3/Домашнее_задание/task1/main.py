def list_of_numbers():
    n = int(input("Введите число для формирования ряда:  "))
    list1 = []
    while n >= 0:
        n = int(input("Введите число для формирования ряда:  "))
        if 3 <= n <= 13:
            list1.append(n)
        else:
            continue
    return print(list1)
if __name__ == "__main__":
    print(list_of_numbers())
pass