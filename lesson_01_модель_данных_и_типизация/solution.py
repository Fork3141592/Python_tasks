"""Заготовки для решения. Реализуй функции, затем запусти проверку:
    pytest test_lesson.py -v
"""

# ---- Задача 1.1: Псевдоним или копия ----
def make_pair(kind):
    original = [1, 2, 3]
    if kind == "alias":
        second = original
        return original,second
    if kind == "copy":
        second = original.copy()
        return original,second

    # TODO: верни (original, second)
    ...

# ---- Задача 1.2: Только настоящие int ----
def only_true_ints(seq):
    ...

# ---- Задача 1.3: Строгая типизация без падений ----
def safe_add(a, b):
    ...

# ---- Задача 1.4: Предскажи вывод (ссылочная модель) ----
def predicted():
    # верни строку — то, что напечатает print(y)
    ...

