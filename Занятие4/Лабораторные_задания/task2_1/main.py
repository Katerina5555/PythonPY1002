if __name__ == "__main__":
    a = 21345
    list_of_numbers = [int(x) for x in str(a)]
    print(list_of_numbers)
    print(sum(list_of_numbers))
    print(sum([i for i in list_of_numbers if i % 2 == 0]))
    print(len(list_of_numbers))
    print(f"5 min: {min(list_of_numbers)} max: {max(list_of_numbers)}")
    print([list_of_numbers[index] for index in range(len(list_of_numbers)) if index % 2 == 0])    #четные по индексу
    print(list_of_numbers[0] - list_of_numbers[-1])
    print(f"8 min: {min(list_of_numbers)} position: {list_of_numbers.index(min(list_of_numbers))} ")    #индекс с 0
    pass
