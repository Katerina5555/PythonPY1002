def remove_whitespace(str_):
    word_str_ = str_.split(" ")    # TODO с помощью методов строки join и split очистить строку от лишних пробелов
    print(word_str_)

    word_no_empty = []
    for elem in word_str_:
        if len(elem) > 0:
            word_no_empty.append(elem)
    return " ".join(word_no_empty)
if __name__ == "__main__":
    str_with_space = "    123.    test   print test11    "  # исходная строка
    print(remove_whitespace(str_with_space))
