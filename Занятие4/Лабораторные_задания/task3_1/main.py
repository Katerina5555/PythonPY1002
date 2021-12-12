# TODO
from collections import Counter     #ИСПОЛЬЗОВАНИЕ КЛАССА COUNTER

def dict_():
    list_of_elements = "Ghtlkjtybt"
    c = Counter(list_of_elements.lower())
    print("Применительно к строке: " + str(list_of_elements))
    if list_of_elements.isalpha():
        print("Все элементы сроки являются буквами")
    else:
        print("В строке имеются элементы помимо букв")
    return dict(c)
def dict_2():
    a = "СегодняЧетверг"
    n_dict = {item: "{:.0%}".format(a.count(item)/len(a)) for item in a.lower()}
    print("Применительно к строке: " + str(a))
    return dict(n_dict.items())

if __name__ == "__main__":
    print(dict_())
    print(dict_2())


