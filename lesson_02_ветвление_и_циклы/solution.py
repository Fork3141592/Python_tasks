"""Заготовки для решения. Реализуй функции, затем запусти проверку:
    pytest test_lesson.py -v
"""
# ---- Задача 2.1: Классификация точки (match-case) ----
def classify(point):
    match point:
        case (0, 0):
            return "origin"
        case (x, 0):               
            return "on-x"
        case (0, y):
            return "on-y"
        case (x, y):        
            return "general"
    ...
# ---- Задача 2.2: Длина последовательности Коллатца ----
def collatz_steps(n):
    steps = 0
    while n != 1:
        if n%2 == 0:
            n = n // 2
            steps += 1
        else:
            n = 3 * n + 1
            steps += 1
    return steps
    ...

# ---- Задача 2.3: Первый повтор ----
def first_duplicate(seq):
    posled = set()
    for x in seq:
        if x in posled:
            return x
        posled.add(x)
    else:
        return None
    ...

# ---- Задача 2.4: Интерпретатор команд (структурные шаблоны) ----
def run(command, pos):
    ...

