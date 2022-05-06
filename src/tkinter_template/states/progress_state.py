import time
import tkinter
from collections import Callable
from threading import Thread
from tkinter import IntVar, StringVar

from tkinter_template.utils.computed import ComputedStringVar


def do_nothing(*arg, **kwds):
    pass


class Computation:
    def __init__(self,
                 on_start: Callable = do_nothing,
                 on_progress: Callable = do_nothing,
                 on_done: Callable = do_nothing
                 ):
        self.on_start = on_start
        self.on_progress = on_progress
        self.on_done = on_done

    def compute(self):
        self.on_start()
        for i in range(100):
            time.sleep(0.1)
            self.on_progress(i + 1)
        self.on_done()


class ProgressState:
    def __init__(self):
        self.progress = IntVar()
        self.completed_text = ComputedStringVar(args=(self.progress,),
                                                f=self.compute_completed_text)
        self.button_state = StringVar(value=tkinter.ACTIVE)

    def start(self):
        self.button_state.set(tkinter.DISABLED)
        computation = Computation(
            on_progress=self.progress.set,
            on_done=lambda: self.button_state.set(tkinter.ACTIVE))
        thread = Thread(target=computation.compute)
        thread.start()

    def compute_completed_text(self, *args):
        if self.progress.get() == 0:
            return 'Not Started'
        elif self.progress.get() < 100:
            return f'Working {self.progress.get()}%'
        else:
            return 'Done'
