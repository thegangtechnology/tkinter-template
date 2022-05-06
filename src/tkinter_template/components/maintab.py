import tkinter as tk
from tkinter import ttk

from tkinter_template.components.progress import Progress
from tkinter_template.components.randomizer import Randomizer
from tkinter_template.components.string_concatenator import StringConcatenator
from tkinter_template.states import State


class MainTab(ttk.Notebook):
    def __init__(self, root: tk.BaseWidget, **kwds):
        super().__init__(root)
        self.sc = StringConcatenator(self)
        self.sc.pack()
        self.add(self.sc, text='Concatenator')

        self.randomizer = Randomizer(self)
        self.randomizer.pack()
        self.add(self.randomizer, text='Randomizer')

        self.progress = Progress(self)
        self.progress.pack()
        self.add(self.progress, text='Progress')

    def subscribe(self, st: State):
        self.sc.subscribe(st.concatenator_state)
        self.randomizer.subscribe(st.randomizer_state)
        self.progress.subscribe(st.progress_state)
