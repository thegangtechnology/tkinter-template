import tkinter as tk
from tkinter import ttk

from tkinter_template.components.string_concatenator import StringConcatenator
from tkinter_template.states import State
from tkinter_template.utils import GridPlacer as gp


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.state = State()

        tabs = ttk.Notebook(self)
        gp.stretch_both(tabs, 0, 0)

        sc = StringConcatenator(tabs)
        sc.pack()
        sc.subscribe(prefix=self.state.prefix,
                     suffix=self.state.suffix,
                     full_string=self.state.full_string)
        tabs.add(sc, text='Concatenator')
