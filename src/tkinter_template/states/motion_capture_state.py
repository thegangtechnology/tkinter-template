import tkinter
from tkinter import IntVar

from tkinter_template.utils.computed import ComputedStringVar


class MotionCaptureState:
    def __init__(self):
        self.x = IntVar(value=0)
        self.y = IntVar(value=0)

        self.full_text = ComputedStringVar((self.x, self.y),
                                           f=lambda x, y: f'Last Mouse: ({x}, {y})')

    def on_move(self, ev: tkinter.Event):
        # print(ev, ev.x, ev.y, ev.x_root, ev.y_root)
        # if you want to see the attribute in ev just print(dir(ev))
        self.x.set(ev.x)
        self.y.set(ev.y)
