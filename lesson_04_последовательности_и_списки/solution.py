"""Заготовки для решения. Реализуй функции, затем запусти проверку:
    pytest test_lesson.py -v
"""

# ---- Задача 4.1: Вставка через срез ----
def insert_at(lst, i, items):
    return lst[:i] + items + lst[i:]
    ...

# ---- Задача 4.2: Независимая таблица ----
def make_grid(rows, cols):
    return [[0] * cols for x in range(rows)]

# ---- Задача 4.3: Через один задом наперёд ----
def every_other_reversed(lst):
    lst = lst[::-1]
    lst = lst[::2]
    return lst
    ...

# ---- Задача 4.4: Разгладить на один уровень ----
def flatten_once(nested):
    lst = []
    for i in nested:
        lst += i
    return lst
    ...

