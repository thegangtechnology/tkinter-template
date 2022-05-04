import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)
from matplotlib.figure import Figure

from tkinter_template.states import RandomizerState
from tkinter_template.utils import GridPlacer


class RandomizerSideBar(tk.Frame):
    def __init__(self, root: tk.BaseWidget, **kwds):
        super().__init__(root, **kwds)
        self.mean_entry = ttk.Scale(self, from_=-5, to=5)
        self.mean_entry.grid(row=0)

        self.width_entry = ttk.Scale(self, from_=-2, to=2)
        self.width_entry.grid(row=1)

        self.n_entry = ttk.Scale(self, from_=5, to=5000, value=5)
        self.n_entry.grid(row=2)

        self.do_it_button = ttk.Button(self, text='hello')
        self.do_it_button.grid(row=3)

    def subscribe(self, st: RandomizerState):
        self.mean_entry.config(variable=st.mean)
        self.width_entry.config(variable=st.width)
        self.n_entry.config(variable=st.n)
        self.do_it_button.config(command=st.do_randomize)


class Randomizer(tk.Frame):
    def __init__(self, root: tk.BaseWidget, **kwds):
        super().__init__(root, **kwds)
        # note no binding, it's important to separate the look from the interaction
        self.sidebar = RandomizerSideBar(self)
        GridPlacer.stretch_y(self.sidebar, row=0, column=0, sticky='n')

        fig = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        GridPlacer.stretch_both(self.canvas.get_tk_widget(), row=0, column=1)
        self.canvas.draw_idle()

    def refresh_figure(self):
        self.canvas.draw_idle()

    def subscribe(self, st: RandomizerState):
        self.sidebar.subscribe(st)
        st.fig.set(self.canvas.figure)
        st.fig.trace_add(self.refresh_figure)
