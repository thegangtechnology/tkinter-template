from tkinter import StringVar
from typing import TypeVar

T = TypeVar('T')


class FullString(StringVar):  # this is how you should do computed state
    def __init__(self, prefix: StringVar, suffix: StringVar):
        super().__init__()
        self.prefix = self.subscribe(prefix)
        self.suffix = self.subscribe(suffix)

    def update(self, var_name: str, var_index: str, operation: str):
        full_string = self.prefix.get() + self.suffix.get()
        self.set(full_string)

    def subscribe(self, var: T, mode='write') -> T:
        var.trace_add(mode, self.update)
        return var


class ConcatenatorState:
    def __init__(self):
        self.prefix = StringVar()
        self.suffix = StringVar()
        self.full_string = FullString(self.prefix, self.suffix)
