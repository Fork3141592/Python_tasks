# -*- coding: utf-8 -*-
import pytest
import solution as sol

# ---- Задача 2.1: Классификация точки (match-case) ----
def test_task_1():
    assert sol.classify((0, 0)) == "origin"
    assert sol.classify((0, 5)) == "on-y"
    assert sol.classify((5, 0)) == "on-x"
    assert sol.classify((3, 4)) == "general"

# ---- Задача 2.2: Длина последовательности Коллатца ----
def test_task_2():
    assert sol.collatz_steps(1) == 0
    assert sol.collatz_steps(2) == 1
    assert sol.collatz_steps(3) == 7
    assert sol.collatz_steps(27) == 111

# ---- Задача 2.3: Первый повтор ----
def test_task_3():
    assert sol.first_duplicate([1, 2, 3, 2, 1]) == 2
    assert sol.first_duplicate([1, 2, 3]) is None
    assert sol.first_duplicate([]) is None
    assert sol.first_duplicate(["a", "b", "a"]) == "a"

# ---- Задача 2.4: Интерпретатор команд (структурные шаблоны) ----
def test_task_4():
    assert sol.run(["move", "up", 3], (0, 0)) == (0, 3)
    assert sol.run(["move", "left", 2], (5, 5)) == (3, 5)
    assert sol.run(["reset"], (7, 7)) == (0, 0)
    assert sol.run(["jump"], (7, 7)) == (7, 7)
    assert sol.run(["move", "up", "x"], (0, 0)) == (0, 0)

