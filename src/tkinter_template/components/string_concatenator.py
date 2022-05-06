import tkinter as tk
from tkinter import ttk, StringVar

from tkinter_template.states import ConcatenatorState
from tkinter_template.utils import GridPlacer as gp
from tkinter_template.utils.computed import bind_to_prop


class StringConcatenator(tk.Frame):
    def __init__(self, root: tk.BaseWidget, **kwds):
        super().__init__(root, **kwds)
        # note no binding, it's important to separate the look from the interaction
        self.prefix_entry = ttk.Entry(self)
        gp.stretch_x(self.prefix_entry, row=0, column=0, min_width=100)

        self.suffix_entry = ttk.Entry(self)
        gp.stretch_x(self.suffix_entry, row=1, column=0)

        self.full_string_label = tk.Label(self)
        gp.stretch_x(self.full_string_label, row=2, column=0)

        self.full_string_short_label = tk.Label(self)
        gp.stretch_x(self.full_string_short_label, row=3, column=0)

    def subscribe(self, st: ConcatenatorState):
        self.suffix_entry.config(textvariable=st.suffix)
        self.prefix_entry.config(textvariable=st.prefix)
        self.full_string_label.config(textvariable=st.full_string)
        self.full_string_short_label.config(textvariable=st.full_string_short)
        bind_to_prop(self.full_string_label, 'bg', st.color)
