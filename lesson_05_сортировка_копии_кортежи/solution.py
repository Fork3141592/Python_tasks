"""Заготовки для решения. Реализуй функции, затем запусти проверку:
pytest test_lesson.py -v
"""

from typing import Any


# ---- Задача 5.1: Сортировка по длине, потом по алфавиту ----
def sort_words(words: list[str]) -> list[str]: ...


# ---- Задача 5.2: Таблица лидеров (стабильность сортировки) ----
def leaderboard(rows: list[tuple[str, int]]) -> list[tuple[str, int]]: ...


# ---- Задача 5.3: Настоящая независимая копия ----
import copy


def independent_copy(matrix: list[list[int]]) -> list[list[int]]: ...


# ---- Задача 5.4: Неизменяемый кортеж с изменяемым нутром ----
def append_to_tuple_list(t: tuple[list[Any], Any], x: Any) -> tuple[list[Any], Any]: ...
