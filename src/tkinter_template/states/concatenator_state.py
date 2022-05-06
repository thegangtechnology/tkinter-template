from tkinter import StringVar
from typing import TypeVar

from tkinter_template.utils.computed import ComputedStringVar, Computed

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
        self.full_string_short = ComputedStringVar(args=(self.prefix, self.suffix),
                                                   f=self.get_full_string)
        self.color = Computed[str](args=(self.prefix, self.suffix),
                                   f=self.get_color)
        # computed (not computedVar doesn't work like tkinter variable (can't be bind like internal tkvariable)
        # it can be used to bind with non variable prop

    def get_full_string(self, prefix: str, suffix: str) -> str:
        return 'short' + prefix + suffix

    def get_color(self, *args) -> str:
        t = len(self.prefix.get()) > len(self.suffix.get())
        return 'red' if t else 'green'
