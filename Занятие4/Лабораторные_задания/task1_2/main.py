def nc_sqrt(n, m):
    return [i ** 2 for i in range(n, m+1, 1) if i % 2 != 0]

if __name__ == "__main__":
    print(nc_sqrt(1, 9))