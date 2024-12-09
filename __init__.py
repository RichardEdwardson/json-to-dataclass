__version__ = "1.1.0"
__all__ = ["json_to_dataclass", "decoder"]
__author__ = "Meiwen Dong <dongmeiwen5583@gmail.com>"

import json
from typing import Any
from utils import decoder


def json_to_dataclass(data_json: str) -> Any:
    return json.loads(data_json, object_hook=decoder)
