def fun_2():
    def sort_rule(x):
        return x[1]
    a = 123453
    list_of_numbers = [int(d) for d in str(a)]
    x_dict = {int(x): list_of_numbers.count(x) for x in list_of_numbers}
    sort_ = sorted(x_dict.items(), key=sort_rule)[-1:]
    # print(sort_)    # для проверки
    sort_1 = list(sort_[0])
    # print(sort_1[-1])    # для проверки
    if sort_1[-1] > 1:
        return "В числе есть одинаковые цифры"
    else:
        return "В числе нет одинаковых цифр"
if __name__ == "__main__":
    print(fun_2())
pass