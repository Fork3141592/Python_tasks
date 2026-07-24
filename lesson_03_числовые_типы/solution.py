"""Заготовки для решения. Реализуй функции, затем запусти проверку:
    pytest test_lesson.py -v
"""
# ---- Задача 3.1: Сравнение float без ловушки ----
import math

def safe_equal(a, b):
    return math.isclose(a, b, rel_tol=1e-5)
    ...

# ---- Задача 3.2: Часы по кругу ----
def clock_add(h, delta):
    h = h + delta
    if h > 23:
        h -= 24
    if h < 0:
        h = 24 + h
    return h
    ...

# ---- Задача 3.3: Большинство голосов ----
def majority(votes):
    votes_za = votes.count(True)
    if votes_za > 1/2 * len(votes):
        return True
    else:
        return False
    ...

# ---- Задача 3.4: coalesce: первый не-None ----
def coalesce(*args):
    for i in args:
        if i is not None:
            return i
    return None
    ...

