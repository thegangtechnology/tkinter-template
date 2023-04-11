import dataclasses
import json
from tkinter import StringVar, BooleanVar

import jmespath
from jmespath.exceptions import ParseError
from tkinter_template.utils import GenericVar
from tkinter_template.utils.computed import Computed, ComputedStringVar


def to_json(obj: object):
    return json.dumps(obj, indent=2)


class CustomFunctions(jmespath.functions.Functions):
    @jmespath.functions.signature({'types': ['object']}, {'types': ['array']})
    def _func_map_merge(self, obj, arg):
        result = []
        for element in arg:
            merged_object = super()._func_merge(obj, element)
            result.append(merged_object)
        return result


options = jmespath.Options(custom_functions=CustomFunctions())


@dataclasses.dataclass
class JmesPathState:

    def __init__(self):
        self.database: GenericVar[object] = GenericVar(None)
        self.result: GenericVar[object] = GenericVar(None)
        self.jmes_path: StringVar = StringVar(value='')
        self.parse_status: BooleanVar = BooleanVar(value=False)
        self.str_database: ComputedStringVar = ComputedStringVar((self.database,), f=to_json)
        self.str_result: ComputedStringVar = ComputedStringVar((self.result,), f=to_json)
        self.bg_color = ComputedStringVar((self.parse_status,), lambda st: 'green' if st else 'red')

    def load_file(self, fname: str):
        with open(fname) as f:
            data = json.load(f)
            self.database.set(data)

    def live_compute(self, print_error=False):
        try:
            self.compute_result()
            self.parse_status.set(True)

        except ParseError as e:
            self.parse_status.set(False)
            if print_error:
                print(e)

    def compute_result(self):
        if len(self.jmes_path.get()) != 0:
            res = jmespath.search(self.jmes_path.get(), self.database.get(), options=options)
            self.result.set(res)
