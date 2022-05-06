import tkinter as tk
from tkinter import ttk

from tkinter_template.states.progress_state import ProgressState
from tkinter_template.utils import SerialVerticalGridPlacer
from tkinter_template.utils.computed import bind_to_prop


class Progress(tk.Frame):

    def __init__(self, root: tk.BaseWidget, **kwds):
        super().__init__(root, **kwds)

        self.progressbar = ttk.Progressbar(self)
        self.label = ttk.Label(self)
        self.status_label = ttk.Label(self)
        self.button = ttk.Button(self, text='Compute')
        gp = SerialVerticalGridPlacer()
        gp.place_stretch_all([self.progressbar,
                              self.label,
                              self.button,
                              self.status_label])

    def subscribe(self, st: ProgressState):
        self.button.config(command=st.start)
        self.label.config(textvariable=st.progress)
        self.status_label.config(textvariable=st.completed_text)
        self.progressbar.config(variable=st.progress)
        bind_to_prop(self.button, 'state', st.button_state)
