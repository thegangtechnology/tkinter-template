from tkinter_template.config.config import Config
from tkinter_template.states.concatenator_state import ConcatenatorState
from tkinter_template.states.many_string_state import ManyStringState
from tkinter_template.states.motion_capture_state import MotionCaptureState
from tkinter_template.states.progress_state import ProgressState
from tkinter_template.states.randomizer_state import RandomizerState


class State:
    def __init__(self, config: Config):
        self.concatenator_state = ConcatenatorState()
        self.randomizer_state = RandomizerState()
        self.progress_state = ProgressState()
        self.motion_capture_state = MotionCaptureState()
        self.many_string_state = ManyStringState(config.variables)
