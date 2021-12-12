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