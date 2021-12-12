def max_len_in_line():
    str1 = input("Enter the line: ")
    list_str1 = str1.split()    # разделение для поиска и вывода списка
    max_len = 0
    list_of_variations = []
    for value in list_str1:    # цикл для поиска максимальной длинны слов/чисел
        if len(value) >= max_len:
            max_len = len(value)
            longest_element = value
            if len(value) == max_len:
                list_of_variations.append(longest_element)    # для цикла исключений
                list_of_longest_value = []
                for value in list(list_of_variations):    # цикл для исключения из списка первых элементов с меньшей длинной, чем последний наибольший из прошлого цикла
                    if len(value) == max_len:
                        max_len = len(value)
                        longest_element = value
                        list_of_longest_value.append(longest_element)

    return list_of_longest_value
if __name__ == "__main__":
    print("The longest elements in a line: " + str(max_len_in_line()))
    pass

def func1(a):
    return max(a.split(), key=len)[::-1]
