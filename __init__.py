__version__ = "1.0.1"
__all__ = ["json_to_dataclass"]
__author__ = "Meiwen Dong <dongmeiwen5583@gmail.com>"

import json
from typing import Any
from dataclasses import make_dataclass


def json_to_dataclass(data_json: str) -> Any:
    data = json.loads(data_json)
    is_data_list: bool = isinstance(data, list)
    is_data_dict: bool = isinstance(data, dict)

    if not (is_data_dict or is_data_list):
        return data

    def unwrapped(value):
        return json_to_dataclass(json.dumps(value))

    if is_data_list:
        return [unwrapped(i) for i in data]
    else:
        json_keys = data.keys()
        for key in json_keys:
            data.update({key: unwrapped(data[key])})

        result_cls = make_dataclass("", json_keys, kw_only=True)
        return result_cls(**data)
