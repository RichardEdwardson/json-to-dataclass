__version__ = "1.0.0"
__all__ = ["json_to_dataclass"]
__author__ = "Meiwen Dong <dongmeiwen5583@gmail.com>"

import json
from typing import Any
from dataclasses import make_dataclass


def json_to_dataclass(data_json: str) -> Any:
    data = json.loads(data_json)
    if isinstance(data, list):
        return [json_to_dataclass(json.dumps(i)) for i in data]
    elif isinstance(data, dict):
        params_spec = []
        for key in data.keys():
            value = data[key]
            value_unwrapped = json_to_dataclass(json.dumps(value))
            data.update({key: value_unwrapped})
            params_spec.append((key, type(value_unwrapped)))

        result_cls = make_dataclass("", params_spec, kw_only=True)
        return result_cls(**data)
    else:
        return data
