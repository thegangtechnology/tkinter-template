import tkinter as tk
from tkinter import ttk, StringVar

from tkinter_template.utils import GridPlacer as gp


class StringConcatenator(tk.Frame):
    def __init__(self, root: tk.BaseWidget, **kwds):
        super().__init__(root, **kwds)
        # note no binding
        self.prefix_entry = ttk.Entry(self)
        gp.stretch_x(self.prefix_entry, row=0, column=0, min_width=100)

        self.suffix_entry = ttk.Entry(self)
        gp.stretch_x(self.suffix_entry, row=1, column=0)

        self.full_string_label = ttk.Label(self)
        gp.stretch_x(self.full_string_label, row=2, column=0)

    def subscribe(self, prefix: StringVar, suffix: StringVar, full_string: StringVar):
        self.suffix_entry.config(textvariable=suffix)
        self.prefix_entry.config(textvariable=prefix)
        self.full_string_label.config(textvariable=full_string)
