from tkinter import Variable
from typing import TypeVar

from tkinter_template.states.concatenator_state import ConcatenatorState
from tkinter_template.states.progress_state import ProgressState
from tkinter_template.states.randomizer_state import RandomizerState


class State:
    def __init__(self):
        self.concatenator_state = ConcatenatorState()
        self.randomizer_state = RandomizerState()
        self.progress_state = ProgressState()
