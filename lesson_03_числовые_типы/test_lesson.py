# -*- coding: utf-8 -*-
import pytest
import solution as sol


# ---- Задача 3.1: Сравнение ----
def test_task_1():
    assert (0.1 + 0.2 == 0.3) is False
    assert sol.safe_equal(0.1 + 0.2, 0.3) is True
    assert sol.safe_equal(1.0, 1.0) is True
    assert sol.safe_equal(1.0, 1.1) is False


# ---- Задача 3.2: Часы по кругу ----
def test_task_2():
    assert sol.clock_add(23, 3) == 2
    assert sol.clock_add(1, -3) == 22
    assert sol.clock_add(0, -1) == 23
    assert sol.clock_add(12, 0) == 12
    assert sol.clock_add(0, 0) == 0


# ---- Задача 3.3: Большинство голосов ----
def test_task_3():
    assert sol.majority([True, True, False]) is True
    assert sol.majority([True, False]) is False
    assert sol.majority([]) is False
    assert sol.majority([True, True, True]) is True
    assert sol.majority([True, True, False, False]) is False


# ---- Задача 3.4: coalesce: первый не-None ----
def test_task_4():
    assert sol.coalesce(None, 0, 5) == 0
    assert sol.coalesce(None, None, "x") == "x"
    assert sol.coalesce(None, None) is None
    assert sol.coalesce("") == ""
