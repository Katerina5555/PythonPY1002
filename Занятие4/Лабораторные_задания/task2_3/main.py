if __name__ == "__main__":
    a = 945
    list_of_numbers = sum([int(x) for x in str(a)])
    if 10 <= list_of_numbers < 100:
        print("Число двухзначное")
    else:
        print("Число не двухзначное")
pass