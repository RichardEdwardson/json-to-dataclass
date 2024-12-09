# What problem am I solving?

Imagine parsing a JSON object like

```json
{
    "customer": "BigCo",
    "performances": [
        {
            "playID": "hamlet",
            "audience": 55
        },
        {
            "playID": "as-like",
            "audience": 35
        },
        {
            "playID": "othello",
            "audience": 40
        }
    ]
}
```
How would you access the value of `playID` of the third entry of the `performances` in python?

```python
import json
from above import json_string

serialized_data: dict = json.loads(json_string)
third_play = serialized_data["performances"][2]["playID"]

```
This is how you would normally access value in `dict`. Cumberson, perhaps. But wouldn't it be more intuitive to access it like you would in JavaScript

```python
third_play = serialized_data.performances[2].playID
```
This little library is designed to make this possible, with the help of `dataclasses` library with its python class trickery.