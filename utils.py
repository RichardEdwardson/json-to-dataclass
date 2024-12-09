from dataclasses import make_dataclass
from typing import Any


def decoder(data):
    is_data_list: bool = isinstance(data, list)
    is_data_dict: bool = isinstance(data, dict)

    if not (is_data_dict or is_data_list):
        return data

    def unwrapped(value):
        return decoder(value)

    if is_data_list:
        return [unwrapped(i) for i in data]
    else:
        json_keys = data.keys()
        for key in json_keys:
            data.update({key: unwrapped(data[key])})

        result_cls = make_dataclass("", json_keys, kw_only=True)
        return result_cls(**data)
