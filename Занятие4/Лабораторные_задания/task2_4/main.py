if __name__ == "__main__":
    a = 1123
    list_of_numbers = sum([int(x) for x in str(a)])
    if list_of_numbers % 7 == 0:
        print("Сумма кратна 7")
    else:
        print("Сумма не кратна 7")
pass
