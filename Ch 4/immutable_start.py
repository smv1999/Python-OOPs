# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass

# TODO: "The "frozen" parameter makes the class immutable
@dataclass(frozen= True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def changesomething(self, newval):
        self.value2 = newval


obj = ImmutableClass()
print(obj.value1)
print(obj.value2)

# TODO: attempting to change the value of an immutable class throws an exception
# obj.value1 = "Temp"

# TODO: even functions within the class can't change anything
obj.changesomething(100)
