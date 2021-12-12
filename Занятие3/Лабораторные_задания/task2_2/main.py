def palindrom():
    str1 = input("Enter line: ")
    str_for_check = str1[::-1]
    list_str1 = list(str1)
    list_str_for_check = list(str_for_check)
    for value in list_str1:
        if value == ' ':
            list_str1.remove(value)
    for value in list_str_for_check:
        if value == ' ':
            list_str_for_check.remove(value)
    if list_str1 == list_str_for_check:

        print("Строка является палиндромом")
    else:
        print("Строка не является палиндромом")
    return
if __name__ == "__main__":
    print(palindrom())
    pass