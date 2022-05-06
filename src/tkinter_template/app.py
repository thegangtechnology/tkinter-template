import tkinter as tk

from tkinter_template.components.maintab import MainTab
from tkinter_template.states import State
from tkinter_template.utils import GridPlacer as gp


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.state = State()

        tabs = MainTab(self)
        tabs.subscribe(self.state)
        gp.stretch_both(tabs, 0, 0)
