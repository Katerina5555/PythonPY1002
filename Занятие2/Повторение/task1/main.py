if __name__ == "__main__":
    list_ = list(range(3, 7))  # [3, 4, 5, 6]

    print(list_)
    for value in list_:
        print("Текущее значение элемента списка =",
              value)  # На каждом шаге цикла в переменную value помещается новое значение из списка
    print("-----")
    print("Цикл закончился")
