def task():
    str1 = input("Enter line 1: ")
    str2 = input("Enter line 2: ")
    k = int(input("Enter number: "))
    s1 = []
    s2 = []
    for i in range(0, k, 1):
        s1.append(str1[i])
        s2.append(str2[i])

        if s1 == s2:
            continue
        else:
            continue
    if s1 == s2:
        print("Да")
    else:
        print("Нет")
if __name__ == "__main__":
    print(task())
    pass
