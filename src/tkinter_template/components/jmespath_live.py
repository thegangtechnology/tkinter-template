import tkinter as tk
from tkinter import ttk, filedialog

from tkinter_template.components.text_extension import TextExtension
from tkinter_template.states.jmespath_state import JmesPathState
from tkinter_template.utils import GridPlacer
from tkinter_template.utils.computed import bind_to_prop


class JmesPathFrame(tk.Frame):
    def __init__(self, root: tk.BaseWidget, **kwds):
        super().__init__(root, **kwds)
        self.jmespath_label = tk.Label(self, text="JMESPath")
        self.jmespath = TextExtension(self, height=10)
        GridPlacer.stretch_x(self.jmespath_label, row=0, column=0)
        GridPlacer.stretch_x(self.jmespath, row=1, column=0)


class JmesPathLiveFrame(tk.Frame):
    def __init__(self, root: tk.BaseWidget, **kwds):
        super().__init__(root, **kwds)
        self.raw_data = TextExtension(self)
        GridPlacer.stretch_both(self.raw_data, row=1, column=0)
        self.jmespath_frame = JmesPathFrame(self)
        GridPlacer.stretch_x(self.jmespath_frame, row=0, column=1)

        self.result = TextExtension(self)
        GridPlacer.stretch_both(self.result, row=1, column=1)

        self.button_frame = tk.Frame(self)
        self.load_json_button = ttk.Button(self.button_frame, text="Load JSON")
        GridPlacer.stretch_x(self.load_json_button, row=0, column=0)

        self.doit_button = ttk.Button(self.button_frame, text="Flatten")
        GridPlacer.stretch_x(self.doit_button, row=1, column=0)
        self.status_label = tk.Label(self.button_frame)
        GridPlacer.stretch_x(self.status_label, row=2, column=0)
        self.error_log = TextExtension(self.button_frame, height=5)
        GridPlacer.stretch_x(self.error_log, row=3, column=0)

        GridPlacer.stretch_x(self.button_frame, row=0, column=0)

    def subscribe(self, st: JmesPathState):
        self.raw_data.config(textvariable=st.str_database)
        self.jmespath_frame.jmespath.config(textvariable=st.jmes_path)
        self.result.config(textvariable=st.str_result)
        self.doit_button.config(command=st.live_compute)
        st.jmes_path.trace_add('write', lambda *arg: st.live_compute())

        def do_load_json():
            filename = filedialog.askopenfilename(defaultextension='json')
            st.load_file(filename)

        self.load_json_button.config(command=do_load_json)
        bind_to_prop(self.status_label, 'bg', st.bg_color)
        self.error_log.config(textvariable=st.error_text)
