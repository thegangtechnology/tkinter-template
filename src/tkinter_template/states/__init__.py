from tkinter import DoubleVar, Variable, StringVar
from typing import TypeVar

T = TypeVar('T', bound=Variable)

class FullString(StringVar): # this is how you should do computed state
    def __init__(self, prefix: StringVar, suffix: StringVar):
        super().__init__()
        self.prefix = self.subscribe(prefix)
        self.suffix = self.subscribe(suffix)

    def update(self, varname: str, varindex: str, operation: str):
        power = self.prefix.get() + self.suffix.get()
        self.set(power)

    def subscribe(self, var: T, mode='write') -> T:
        var.trace_add(mode, self.update)
        return var

class State:
    def __init__(self):
        self.prefix = StringVar()
        self.suffix = StringVar()
        self.full_string = FullString(self.prefix, self.suffix)
