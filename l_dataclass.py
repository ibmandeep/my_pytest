# dataclasses is a module introduced in Python 3.7 that provides a decorator and functions for automatically adding 
# special methods (like __init__, __repr__, __eq__, etc.) to user-defined classes — without writing boilerplate code.


from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

# Create an instance
b = Book("Python Basics", "John Doe", 300, 29.99)

# Automatically provides __repr__, __eq__, etc.
print(b)  # Book(title='Python Basics', author='John Doe', pages=300, price=29.99)
print(b.title)


# With Default Values
@dataclass
class User:
    name: str
    active: bool = True

u = User("Mandeep") 
print(u)   


# Make Class Immutable (frozen=True)
@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
# p.x = 10  # Will raise FrozenInstanceError


# Field Customization with field()
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    tags: list[str] = field(default_factory=list)