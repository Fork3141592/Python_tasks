"""Заготовки для решения. Реализуй функции, затем запусти проверку:
pytest test_lesson.py -v
"""


# ---- Задача 6.1: Длина: escape против r-строки ----
def escape_lengths():
    return (3,4)
    # верни кортеж из двух длин
    ...


# ---- Задача 6.2: Замена символа в строке ----
def replace_at(s: str, i: int, ch: str) -> str: 
    s = s[:i] + ch + s[i+1:]
    return s
    ...


# ---- Задача 6.3: Шифр Цезаря ----
def caesar(s: str, k: int) -> str:
    alfa = "abcdefghijklmnopqrstuvwxyz"
    s_new = ""

    for i in s:
        if i in alfa:
            i_new = (alfa.index(i) + k) % 26
            s_new += alfa[i_new]
        else:
            s_new += i
    return s_new
    ...


# ---- Задача 6.4: Отсортирован ли по алфавиту ----
def is_sorted_words(words: list[str]) -> bool: 
    return sorted(words)== words
    ...
