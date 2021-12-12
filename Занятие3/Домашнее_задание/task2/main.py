def check_string():
    base = set('01')
    str_ = str(input("Введите число для проверки: "))
    for d in set(str_):  # выделяем все уникальные символы из строки
        if d not in base:
            return False
    return True

if __name__ == "__main__":
    print(check_string())
    pass
