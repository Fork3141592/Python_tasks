# -*- coding: utf-8 -*-
import pytest
import solution as sol

# ---- Задача 1.1: Псевдоним или копия ----
def test_task_1_alias():
    o, s = sol.make_pair("alias")
    assert s is o
    o.append(4)
    assert s == [1, 2, 3, 4]

def test_task_1_copy():
    o, s = sol.make_pair("copy")
    assert s is not o
    assert s == o
    o.append(4)
    assert s == [1, 2, 3]

# ---- Задача 1.2: Только настоящие int ----
def test_task_2():
    assert sol.only_true_ints([1, True, 2, False, 3]) == [1, 2, 3]
    assert sol.only_true_ints([True, False]) == []
    assert sol.only_true_ints([0, 1, 2.0, "3"]) == [0, 1]

# ---- Задача 1.3: Строгая типизация без падений ----
def test_task_3():
    assert sol.safe_add(1, 2) == 3
    assert sol.safe_add("a", "b") == "ab"
    assert sol.safe_add([1], [2]) == [1, 2]
    assert sol.safe_add(1, "b") is None
    assert sol.safe_add(None, 1) is None

# ---- Задача 1.4: Предскажи вывод (ссылочная модель) ----
def test_task_4():
    x = [1, 2, 3]
    y = x
    def f(z):
        z = z + [4]
        return z
    f(x)
    x.append(99)
    assert sol.predicted() == str(y)

