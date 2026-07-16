# -*- coding: utf-8 -*-
import pytest
import solution as sol

# ---- Задача 7.1: Процент с одним знаком ----
def test_task_1():
    assert sol.pct(3, 7) == "42.9%"
    assert sol.pct(1, 4) == "25.0%"
    assert sol.pct(1, 1) == "100.0%"

# ---- Задача 7.2: Надёжность пароля ----
def test_task_2():
    assert sol.is_strong("Abcdef12") is True
    assert sol.is_strong("abcdef12") is False
    assert sol.is_strong("Abc12") is False
    assert sol.is_strong("ABCDEF12") is False

# ---- Задача 7.3: Разбор конфигурации ----
def test_task_3():
    assert sol.parse_config("a = 1; b = hello world ") == {"a": "1", "b": "hello world"}
    assert sol.parse_config("x=1;") == {"x": "1"}
    assert sol.parse_config("") == {}

# ---- Задача 7.4: Перекрывающиеся вхождения ----
def test_task_4():
    assert sol.count_overlapping("aaaa", "aa") == 3
    assert sol.count_overlapping("abcabc", "abc") == 2
    assert sol.count_overlapping("aaa", "b") == 0
    assert sol.count_overlapping("xyz", "") == 0

