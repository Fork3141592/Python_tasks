# -*- coding: utf-8 -*-
import pytest
import solution as sol


# ---- Задача 4.1: Вставка через срез ----
def test_task_1():
    assert sol.insert_at([1, 2, 3], 1, [8, 9]) == [1, 8, 9, 2, 3]
    src = [1, 2, 3]
    assert sol.insert_at(src, 0, [0]) == [0, 1, 2, 3]
    assert src == [1, 2, 3]


# ---- Задача 4.2: Независимая таблица ----
def test_task_2():
    g = sol.make_grid(2, 3)
    assert g == [[0, 0, 0], [0, 0, 0]]
    g[0][0] = 1
    assert g[1][0] == 0


# ---- Задача 4.3: Через один задом наперёд ----
def test_task_3():
    assert sol.every_other_reversed([0, 1, 2, 3, 4, 5]) == [5, 3, 1]
    assert sol.every_other_reversed([1]) == [1]
    assert sol.every_other_reversed([]) == []


# ---- Задача 4.4: Разгладить на один уровень ----
def test_task_4():
    assert sol.flatten_once([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert sol.flatten_once([]) == []
    assert sol.flatten_once([[1], []]) == [1]
