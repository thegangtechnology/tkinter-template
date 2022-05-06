from tkinter import DoubleVar, IntVar, StringVar

import numpy as np
from matplotlib.figure import Figure

from tkinter_template.utils import GenericVar


class RandomizerState:
    def __init__(self):
        self.mean = DoubleVar(value=3)
        self.width = DoubleVar(value=2)
        self.n = IntVar(value=100)

        self.event  = StringVar()

        self.data: GenericVar[np.ndarray] = GenericVar()
        self.fig: GenericVar[Figure] = GenericVar()

    def do_randomize(self):
        mean = self.mean.get()
        width = self.width.get()
        n = self.n.get()
        data = np.random.randn(n) * width + mean
        self.data.set(data)
        self.make_hist()

    def make_hist(self):
        # All these for the fact that tkagg canvas doesn't support assignment of fig..??
        figure: Figure = self.fig.get()
        figure.clear()
        figure.add_subplot(111).hist(self.data.get())
        self.fig.trigger()

    def on_click(self, ev):
        self.event.set(f'(x,y): {ev.x},{ev.y} | (xdata,ydata): {ev.xdata},{ev.ydata} ')
