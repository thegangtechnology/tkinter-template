import tkinter as tk
from tkinter import ttk

from tkinter_template.components.randomizer import Randomizer
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
        sc.subscribe(self.state.concatenator_state)
        tabs.add(sc, text='Concatenator')

        randomizer = Randomizer(tabs)
        randomizer.pack()
        randomizer.subscribe(self.state.randomizer_state)
        tabs.add(randomizer, text='Randomizer')
