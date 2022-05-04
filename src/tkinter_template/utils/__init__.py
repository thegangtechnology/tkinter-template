import tkinter as tk
from typing import Optional, Generic, List, Callable, TypeVar

T = TypeVar('T')


class GridPlacer:
    @classmethod
    def stretch_both(cls,
                     widget: tk.Widget,
                     row: int,
                     column: int,
                     min_width: Optional[int] = None,
                     min_height: Optional[int] = None,
                     **kwds):
        opt = {'sticky': 'nsew'} | kwds
        widget.grid(row=row, column=column, **opt)
        widget.master.grid_columnconfigure(column, weight=1, minsize=min_width)
        widget.master.grid_rowconfigure(row, weight=1, minsize=min_height)

    @classmethod
    def stretch_x(cls, widget: tk.Widget, row: int, column: int, min_width=None, **kwds):
        opt = {'sticky': 'ew'} | kwds
        widget.grid(row=row, column=column, **opt)
        widget.master.grid_columnconfigure(column, weight=1, minsize=min_width)
        widget.master.grid_rowconfigure(row, weight=0)

    @classmethod
    def stretch_y(cls, widget: tk.Widget, row: int, column: int, min_height=None, **kwds):
        opt = {'sticky': 'ns'} | kwds
        widget.grid(row=row, column=column, **opt)
        widget.master.grid_columnconfigure(column, weight=0)
        widget.master.grid_rowconfigure(row, weight=1, minsize=min_height)


class GenericVar(Generic[T]):
    def __init__(self):
        self.value: Optional[T] = None
        self._callbacks: List[Callable] = []

    def get(self) -> T:
        return self.value

    def set(self, value: Optional[T]):
        self.value = value
        self.trigger()

    def trigger(self):
        for cb in self._callbacks:
            cb()

    def trace_add(self, cb: Callable):
        self._callbacks.append(cb)
