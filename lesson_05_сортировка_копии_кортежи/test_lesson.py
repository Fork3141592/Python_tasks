# -*- coding: utf-8 -*-
import pytest
import solution as sol

# ---- Задача 5.1: Сортировка по длине, потом по алфавиту ----
def test_task_1():
    assert sol.sort_words(["bb", "a", "ccc", "aa"]) == ["a", "aa", "bb", "ccc"]
    assert sol.sort_words([]) == []

# ---- Задача 5.2: Таблица лидеров (стабильность сортировки) ----
def test_task_2():
    data = [("bob", 10), ("ann", 20), ("cat", 10)]
    assert sol.leaderboard(data) == [("ann", 20), ("bob", 10), ("cat", 10)]

# ---- Задача 5.3: Настоящая независимая копия ----
def test_task_3():
    m = [[1, 2], [3, 4]]
    c = sol.independent_copy(m)
    c[0][0] = 99
    assert m == [[1, 2], [3, 4]]
    assert c == [[99, 2], [3, 4]]

# ---- Задача 5.4: Неизменяемый кортеж с изменяемым нутром ----
def test_task_4():
    t = ([1, 2], 3)
    r = sol.append_to_tuple_list(t, 9)
    assert r is t
    assert r == ([1, 2, 9], 3)

