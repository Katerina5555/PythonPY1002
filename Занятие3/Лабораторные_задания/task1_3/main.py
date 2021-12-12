n = 19
def simple_list(n):
    if n == 1:
        return [1]
    list_ = []
    i = 2
    while n != 1:
        if n % i == 0:
            n = n // i
            list_.append(i)
            continue
        i += 1
    return list_
if __name__ == "__main__":
    print(simple_list(n))    # Write your solution here
    pass
