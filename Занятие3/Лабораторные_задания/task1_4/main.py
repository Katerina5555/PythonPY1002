n = 1
def sum_1(n):
    list_ = []
    epsilon_ = 0.0001
    while (1/(2 ** n)) >= epsilon_:
        list_.append(1/(2 ** n))
        n += 1
    return sum(list_)

if __name__ == "__main__":
    print(sum_1(n))

pass
