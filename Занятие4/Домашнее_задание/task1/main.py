def fun_1():
    a = 111111
    list_of_numbers = [int(d) for d in str(a)]
    b = len(str(a))
    for x in range(1, b, 1):
        if list_of_numbers[x] == list_of_numbers[0]:
            return True
        else:
            return False
if __name__ == "__main__":
    print(fun_1())
pass
