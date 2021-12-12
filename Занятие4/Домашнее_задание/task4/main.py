def happy_():
    a = 123411
    list_a = [int(d) for d in str(a)]
    if len(list_a) == 6:
        if sum(list_a[:3:]) == sum(list_a[3::]):    # сравнение срезов
            return ("Число " + str(a) + " - счастливое.")
        else:
            return ("Число " + str(a) + " - несчастливое.")
    else:
        return "Введенное число не соответствует параметрам."

if __name__ == "__main__":
    print(happy_())
    pass

