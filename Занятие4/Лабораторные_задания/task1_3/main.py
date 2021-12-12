def find_nc_number(n, m):
    return len([i for i in range(n, m + 1, 1) if i % 2 == 0])

if __name__ == "__main__":
    print(find_nc_number(4, 14))

