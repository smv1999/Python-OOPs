# implementing default values in data classes

from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,40))

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0 
    # price: float = field(default=10.0)
    price: float = field(default_factory=price_func)
    

b1 = Book()


# data class automatically creates the __str__ and __repr__ methods
b1 = Book("Wings of Fire", "APJ Abdul Kalam", 1003)
print(b1)
# print(repr(b1))



