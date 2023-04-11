import tkinter as tk
from typing import List

from tkinter_template.utils.computed import ComputedStringVar


class ManyStringState:
    def __init__(self, variables: List[str]):
        self.variable_states = {v: tk.StringVar(value='') for v in variables}
        self.total_length = ComputedStringVar(args=tuple(self.variable_states.values()),
                                              f=self.compute_total_length)

    def compute_total_length(self, *variables):
        return sum(map(len, variables))
