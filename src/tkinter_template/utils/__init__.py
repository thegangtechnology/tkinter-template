import tkinter as tk
from typing import Optional, Generic, List, Callable, TypeVar, Sequence

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
    def __init__(self, value:Optional[T]=None):
        self.value: Optional[T] = value
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

class SerialVerticalGridPlacer:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col

    def place(self, widget: tk.Widget):
        widget.grid(row=self.row)
        self.row+=1

    def place_all(self, widgets: Sequence[tk.Widget]):
        for w in widgets:
            self.place(w)

    def place_stretch(self, widget: tk.Widget):
        GridPlacer.stretch_x(widget, row=self.row, column=self.col)
        self.row += 1

    def place_stretch_all(self, widgets:  Sequence[tk.Widget]):
        for w in widgets:
            self.place_stretch(w)
