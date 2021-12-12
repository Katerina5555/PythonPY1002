S = int(input("Накоплено (руб):  "))
A = int(input("Стипендия за месяц (руб):  "))
B = int(input("Сумма расходов на проживание в первый месяц (руб):  "))
def sum_1():
    list_ = []
    n = 0
    for n in range(0, 100, 1):
        while sum(list_) < ((n+1) * A + S):
            list_.append((B * (105 / 100) ** int(n)))

    return int(len(list_)-1)

if __name__ == "__main__":
    print("На накопления и степендию можно прожить " + str(sum_1()) + " полный(х) месяца(ев).")

pass
