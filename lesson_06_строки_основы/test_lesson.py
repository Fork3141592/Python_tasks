# -*- coding: utf-8 -*-
import pytest
import solution as sol


# ---- Задача 6.1: Длина: escape против r-строки ----
def test_task_1():
    assert sol.escape_lengths() == (len("a\tb"), len(r"a\tb"))


# ---- Задача 6.2: Замена символа в строке ----
def test_task_2():
    assert sol.replace_at("hello", 0, "H") == "Hello"
    assert sol.replace_at("cat", 2, "r") == "car"


# ---- Задача 6.3: Шифр Цезаря ----
def test_task_3():
    assert sol.caesar("abc", 1) == "bcd"
    assert sol.caesar("xyz", 3) == "abc"
    assert sol.caesar("a b", 1) == "b c"
    assert sol.caesar("hello", 0) == "hello"
    assert sol.caesar("a/b-c!", 4) == "e/f-g!"


# ---- Задача 6.4: Отсортирован ли по алфавиту ----
def test_task_4():
    assert sol.is_sorted_words(["a", "b", "c"]) is True
    assert sol.is_sorted_words(["b", "a"]) is False
    assert sol.is_sorted_words(["Z", "a"]) is True
    assert sol.is_sorted_words([]) is True
