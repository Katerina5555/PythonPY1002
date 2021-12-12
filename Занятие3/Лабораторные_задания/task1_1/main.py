def main():
    list_of_sqrt = []
    count = 0
    while sum(list_of_sqrt) <= 500:
        list_of_sqrt.append(count**2)
        count += 1
    return len(list_of_sqrt) - 1

if __name__ == "__main__":
      print(main())

pass
