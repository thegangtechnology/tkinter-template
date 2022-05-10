import tkinter as tk
from tkinter import ttk
from typing import Tuple

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)
from matplotlib.figure import Figure

from tkinter_template.states import RandomizerState
from tkinter_template.utils import GridPlacer, SerialVerticalGridPlacer


class RandomizerSideBar(tk.Frame):
    def __init__(self, root: tk.BaseWidget, **kwds):
        super().__init__(root, **kwds)
        gp = SerialVerticalGridPlacer()
        self.mean_label = ttk.Label(self, text='Mean')
        self.mean_entry = ttk.Scale(self, from_=-5, to=5)
        gp.place_all([self.mean_label, self.mean_entry])

        self.width_label = ttk.Label(self, text='Width')
        self.width_entry = ttk.Scale(self, from_=-2, to=2)
        gp.place_all([self.width_label, self.width_entry])

        self.n_label = ttk.Label(self, text='N')
        self.n_entry = ttk.Scale(self, from_=5, to=5000, value=5)
        gp.place_all([self.n_label, self.n_entry])

        self.do_it_button = ttk.Button(self, text='Random')
        gp.place(self.do_it_button)

    def subscribe(self, st: RandomizerState):
        self.mean_entry.config(variable=st.mean)
        self.width_entry.config(variable=st.width)
        self.n_entry.config(variable=st.n)
        self.do_it_button.config(command=st.do_randomize)


class MPLCanvas(FigureCanvasTkAgg):
    def __init__(self, master, figsize: Tuple[int, int] = (5, 4), dpi=100, **kwds):
        figure = Figure(figsize=figsize, dpi=dpi)
        super().__init__(figure, master, **kwds)


class Randomizer(tk.Frame):
    def __init__(self, root: tk.BaseWidget, **kwds):
        super().__init__(root, **kwds)
        # note no binding, it's important to separate the look from the interaction
        self.sidebar = RandomizerSideBar(self)
        GridPlacer.stretch_y(self.sidebar, row=0, column=0, sticky='n')

        self.canvas = MPLCanvas(self)
        GridPlacer.stretch_both(self.canvas.get_tk_widget(), row=0, column=1)

        self.click_label = ttk.Label(self)
        GridPlacer.stretch_x(self.click_label, row=1, column=1)

    def refresh_figure(self):
        self.canvas.draw_idle()

    def subscribe(self, st: RandomizerState):
        self.sidebar.subscribe(st)
        st.fig.set(self.canvas.figure)
        st.fig.trace_add(self.refresh_figure)
        # https://matplotlib.org/stable/users/explain/event_handling.html
        self.canvas.mpl_connect('button_press_event', st.on_click)
        self.click_label.config(textvariable=st.event)
