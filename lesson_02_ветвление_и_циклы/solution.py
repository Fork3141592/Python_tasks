"""Заготовки для решения. Реализуй функции, затем запусти проверку:
pytest test_lesson.py -v
"""


# ---- Задача 2.1: Классификация точки (match-case) ----
def classify(point): ...


# ---- Задача 2.2: Длина последовательности Коллатца ----
def collatz_steps(n): ...


# ---- Задача 2.3: Первый повтор ----
def first_duplicate(seq): ...


# ---- Задача 2.4: Интерпретатор команд (структурные шаблоны) ----
def run(command, pos):
    x, y = pos
    match command:
        case ["move", ("up" | "down" | "left" | "right") as d, int(steps)]:
            dx, dy = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}[
                d
            ]
            return (x + dx * steps, y + dy * steps)
        case ["reset"]:
            return (0, 0)
        case _:
            return pos
