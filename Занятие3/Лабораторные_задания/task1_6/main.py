a = int(input("Стипендия за месяц (руб):  "))
b = int(input("Сумма расходов на проживание в первый месяц (руб):  "))

def sum_1():
    list_ = []
    for n in range(0, 10, 1):
        list_.append(b * (103 / 100) ** int(n))
    return int(sum(list_)/10) - a

if __name__ == "__main__":
    print("Необходим доп. доход:" + str(sum_1()) + "рублей")

pass
