import tkinter as tk

from tkinter_template.states.motion_capture_state import MotionCaptureState


class MotionCapture(tk.Frame):
    def __init__(self, master: tk.BaseWidget, **kwds):
        super().__init__(master, **kwds)
        self.label = tk.Label(self, text='hello')
        self.label.pack()

    def subscribe(self, st: MotionCaptureState):
        self.label.config(textvariable=st.full_text)
        self.bind('<Motion>', st.on_move)
