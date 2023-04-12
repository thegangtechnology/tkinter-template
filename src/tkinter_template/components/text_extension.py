from tkinter import Frame, StringVar, Variable, Scrollbar, Text, Tk, mainloop, Label

from tkinter.constants import VERTICAL, RIGHT, LEFT, BOTH, END, Y


# modified from https://stackoverflow.com/questions/21507178/tkinter-text-binding-a-variable-to-widget-text-contents
class TextExtension(Frame):
    """Extends Frame.  Intended as a container for a Text field.  Better related data handling
    and has Y scrollbar."""

    def __init__(self, master, textvariable=None, *args, **kwargs):

        super(TextExtension, self).__init__(master)
        # Init GUI

        self._y_scrollbar = Scrollbar(self, orient=VERTICAL)

        self._text_widget = Text(self, yscrollcommand=self._y_scrollbar.set, *args, **kwargs)
        self._text_widget.pack(side=LEFT, fill=BOTH, expand=1)

        self._y_scrollbar.config(command=self._text_widget.yview)
        self._y_scrollbar.pack(side=RIGHT, fill=Y)
        self._text_trace = self._text_widget.bind('<<Modified>>', self.text_modified)
        self._text_variable = None
        self._setup_textvariable(textvariable)

    def _setup_textvariable(self, textvariable: Variable):
        if textvariable is not None:
            if not (isinstance(textvariable, Variable)):
                raise TypeError(
                    "tkinter.Variable type expected, " + str(type(textvariable)) + " given.".format(type(textvariable)))
            self._text_variable = textvariable
            self.var_modified()
            self._var_trace = textvariable.trace("w", self.var_modified)

    def text_modified(self, *args):
        if self._text_variable is not None:
            self._text_variable.trace_vdelete("w", self._var_trace)
            self._text_variable.set(self._text_widget.get(1.0, 'end-1c'))
            self._var_trace = self._text_variable.trace("w", self.var_modified)
            self._text_widget.edit_modified(False)

    def var_modified(self, *args):
        self.set_text(self._text_variable.get())
        self._text_widget.edit_modified(False)

    def unhook(self):
        if self._text_variable is not None:
            self._text_variable.trace_vdelete("w", self._var_trace)
            self._text_variable = None

    def clear(self):
        self._text_widget.delete(1.0, END)

    def set_text(self, _value):
        self.clear()
        if (_value is not None):
            self._text_widget.insert(END, _value)

    def config(self, **kwds):
        if 'textvariable' in kwds:
            self.unhook()
            self._setup_textvariable(kwds['textvariable'])
            del kwds['textvariable']
        return super().config(**kwds)


if __name__ == '__main__':
    root = Tk()
    s = StringVar()
    te = TextExtension(root)
    te.config(textvariable=s)
    te.pack()
    lb = Label(textvariable=s)
    lb.pack()
    mainloop()
