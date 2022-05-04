import tkinter as tk
from typing import Optional


class GridPlacer:
    @classmethod
    def stretch_both(cls,
                     widget: tk.Widget,
                     row: int,
                     column: int,
                     min_width:Optional[int]=None,
                     min_height:Optional[int]=None,
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
