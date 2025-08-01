# Python typing Module
# The typing module in Python provides type hints — a way to specify the expected data types of variables, 
# function arguments, and return values. It helps with readability, linting, refactoring, 
# and tooling like MyPy, pyright, or modern IDEs.


# def greet(name: str) -> str:
#     return f"Hello, {name}"


# | Type              | Usage Example            |
# | ----------------- | ------------------------ |
# | `int`             | `age: int`               |
# | `str`             | `name: str`              |
# | `float`           | `price: float`           |
# | `bool`            | `is_active: bool`        |
# | `list[str]`       | `names: list[str]`       |
# | `dict[str, int]`  | `scores: dict[str, int]` |
# | `tuple[int, str]` | `data: tuple[int, str]`  |
# | `set[int]`        | `ids: set[int]`          |

# from typing import List, Dict, Tuple, Union, Optional, Callable

# def process(scores: List[int]) -> int:
#     return sum(scores)

# def lookup() -> Dict[str, int]:
#     return {"alice": 25}



def add(a: int, b: int) -> int:
    return a + b


c = add('a','a')

print(c)
