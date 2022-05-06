from tkinter import StringVar, IntVar, BooleanVar, Variable, Widget
from typing import Callable, Tuple, TypeVar, Generic, List

T = TypeVar('T')

def bind_to_prop(widget: Widget, prop_name: str, var: Variable):
    def write_prop(*args):
        widget.config(**{prop_name: var.get()}) # this gives some validation
    var.trace_add('write', write_prop)

class ComputedMixin:
    def update(self, *args):
        self.set(self.f(*self.args))

    def subscribe(self, var: T, mode='write') -> T:
        var.trace_add(mode, self.update)
        return var


class ComputedStringVar(StringVar, ComputedMixin):
    def __init__(self, args: Tuple, f: Callable, **kwds):
        super().__init__(**kwds)
        self.args = args
        self.f = f
        for arg in args:
            self.subscribe(arg)
        self.update()


class ComputedBoolVar(BooleanVar, ComputedMixin):
    def __init__(self, args: Tuple, f: Callable, **kwds):
        super().__init__(**kwds)
        self.args = args
        self.f = f
        self.update()
        for arg in args:
            self.subscribe(arg)


class ComputedIntVar(IntVar, ComputedMixin):
    def __init__(self, args: Tuple, f: Callable, **kwds):
        super().__init__(**kwds)
        self.args = args
        self.f = f
        self.update()
        for arg in args:
            self.subscribe(arg)

class Computed(Generic[T], ComputedMixin): # doesn't have all the cool stuff Variable has though
    def __init__(self, args: Tuple, f: Callable, **kwds):
        self.args = args
        self.f = f
        self.cbs: List[Callable] = []
        self.update()
        for arg in args:
            self.subscribe(arg)

    def get(self) -> T:
        return self.value

    def set(self, value: T):
        self.value = value
        for cb in self.cbs:
            cb()

    def trace_add(self, mode: str, callback: Callable):
        self.cbs.append(callback)
