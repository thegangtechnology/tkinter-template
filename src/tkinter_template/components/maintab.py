import tkinter as tk
from tkinter import ttk
from typing import TypeVar

from tkinter_template.components.many_string import ManyString
from tkinter_template.components.motion_capture import MotionCapture
from tkinter_template.components.progress import Progress
from tkinter_template.components.randomizer import Randomizer
from tkinter_template.components.string_concatenator import StringConcatenator
from tkinter_template.config.config import Config
from tkinter_template.states import State

T = TypeVar('T')


class MainTab(ttk.Notebook):
    def __init__(self, root: tk.BaseWidget, config: Config, **kwds):
        super().__init__(root)
        self.sc = self._add_to_tab('Concatenator', StringConcatenator(self))
        self.randomizer = self._add_to_tab('Randomizer', Randomizer(self))
        self.progress = self._add_to_tab('Progress', Progress(self))
        self.motion_capture = self._add_to_tab('Event Capture', MotionCapture(self))

        self.many_string = self._add_to_tab('Many String', ManyString(self, config.variables))

    def _add_to_tab(self, label: str, frame: T) -> T:
        frame.pack()
        self.add(frame, text=label)
        return frame

    def subscribe(self, st: State):
        self.sc.subscribe(st.concatenator_state)
        self.randomizer.subscribe(st.randomizer_state)
        self.progress.subscribe(st.progress_state)
        self.motion_capture.subscribe(st.motion_capture_state)
        self.many_string.subscribe(st.many_string_state)
