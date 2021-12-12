# 7. Напишите функцию search_substr(subst, st), которая принимает 2 строки и определяет,
# имеется ли подстрока subst в строке st.
# В случае нахождения подстроки, возвращается фраза «Есть контакт!», а иначе «Мимо!».
# Должно быть найдено совпадение независимо от регистра обеих строк.

def search_substr(subst, st):
    if subst.lower() in st.lower():
        return 'Есть контакт!'
    else:
        return 'Мимо!'

subst = "привет"
st = "Привет, сегодня прекрасная погода"
print(search_substr(subst, st))

# 8. Требуется определить индексы первого и последнего вхождения буквы в строке.
# Для этого нужно написать функцию first_last(letter, st), включающую 2 параметра:
# letter – искомый символ, st – целевая строка.
# В случае отсутствия буквы в строке, нужно вернуть кортеж (None, None), если же она есть,
# то кортеж будет состоять из первого и последнего индекса этого символа.

def first_last(letter, st):
    str_ = []
    if letter in st:
        str_.append(st.find(letter))
        str_.append(st.rfind(letter))
        return tuple(str_)
    else:
        return tuple((None, None))

letter = "р"
st = "привет, сегодня прекрасная погода"
print(first_last(letter, st))

# 9. На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список, в котором содержатся
# только те числа, которые больше 5 по модулю.

def more_than_five(lst):
    str_ = []
    for n in range(0, len(list(lst)), 1):
        if abs(lst[n]) > 5:
            str_.append(lst[n])
        else:
             continue
    return "В заданной последовательности: " + str(lst) + ", больше пяти по модулю: " + str(str_)

list_ = [15, 5, -10, 26]
print(more_than_five(list_))
