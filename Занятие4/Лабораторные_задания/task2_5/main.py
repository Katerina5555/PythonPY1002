def func_5(a):
    list_of_numbers = [int(x) for x in str(a)]
    if list_of_numbers == list_of_numbers[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    a = 1112113
    print(func_5(a))

pass