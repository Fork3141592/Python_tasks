# Билет 12: Логический тип, синглтоны True/False/None

## Тип bool

`bool` имеет ровно два значения: `True` и `False`. При этом `bool` — **подкласс int**, поэтому:

```python
print(isinstance(True, int))   # True
print(True + True)             # 2
print(True == 1)               # True
print(False == 0)              # True
print(int(True), int(False))   # 1 0
```

## Синглтоны True, False, None

`True`, `False`, `None` — **объекты-синглтоны**: в течение работы программы существует ровно один экземпляр каждого. Поэтому их сравнивают через `is`, а не `==`:

```python
x = None
if x is None:        # ✅ правильно
    ...
if x == None:        # ⚠️ работает, но не рекомендуется
    ...
```

`None` — единственное значение типа `NoneType`, означает «отсутствие значения». Его возвращают функции без `return`.

## Истинностность (truthy / falsy)

Любой объект имеет **логическое представление** — его можно проверить в `if`/`while`. `bool(obj)` даёт это представление.

**Falsy (ложные) значения:**

```python
bool(False)    # False
bool(None)     # False
bool(0)        # False
bool(0.0)      # False
bool("")       # False — пустая строка
bool([])       # False — пустой список
bool({})       # False — пустой словарь
bool(())       # False — пустой кортеж
bool(set())    # False — пустое множество
```

**Truthy:** всё остальное — непустые коллекции, ненулевые числа, любые объекты по умолчанию.

```python
bool(42)       # True
bool("a")      # True
bool([0])      # True — список НЕ пуст (хотя содержит 0!)
```

## Хороший тон проверки

Проверяйте «истинностность» **напрямую**, не сравнивая с `True`/`len`/`0`:

```python
items = [1, 2, 3]

# ✅ Хорошо — питонично
if items:
    ...
if not items:
    ...

# ❌ Плохо — избыточно/хрупко
if items != []:
    ...
if len(items) > 0:
    ...
if items == True:        # вообще неверно: [1,2,3] == True → False!
    ...
```

Для `None` — всегда `is`:

```python
if value is not None:    # ✅
    ...
```

## Итоги

- `bool` — подкласс `int`: `True == 1`, `False == 0`;
- `True`, `False`, `None` — **синглтоны**, сравнивать через `is`;
- falsy: `False None 0 0.0 "" [] {} () set()`; остальное truthy;
- хороший тон: `if items:` вместо `if len(items) > 0:`; `if x is None:`.
