import tkinter as tk
from dataclasses import dataclass
from tkinter import ttk
from typing import List

from tkinter_template.states.many_string_state import ManyStringState


@dataclass
class EntryLabel:
    entry: tk.Entry
    label: tk.Label

    @classmethod
    def empty(cls, master: tk.BaseWidget, text=''):
        return EntryLabel(ttk.Entry(master), ttk.Label(master, text=text))

    def place(self, row_no, column_no=0):
        self.label.grid(row=row_no, column=column_no)
        self.entry.grid(row=row_no, column=column_no + 1)

    def bind(self, textvariable: tk.StringVar):
        self.entry.config(textvariable=textvariable)


class ManyString(tk.Frame):
    def __init__(self, master: tk.BaseWidget, variables: List[str]):
        super().__init__(master)
        self.variable_entries = {v: EntryLabel.empty(self, v) for v in variables}

        self.total_length_label = ttk.Label(self)
        self.total_length_label.grid(row=0, column=0)

        for i, (_, et) in enumerate(self.variable_entries.items(), start=1):
            et.place(i)

    def subscribe(self, vc: ManyStringState):
        for var_name, vs in vc.variable_states.items():
            self.variable_entries[var_name].bind(vs)
        self.total_length_label.config(textvariable=vc.total_length)
