import unittest
import json
from __init__ import json_to_dataclass


class JSON2DataclassTest(unittest.TestCase):
    """
    Assumptions:
        - JSON key does not contain special character or space
    """

    def setUp(self):
        self.create_obj = json_to_dataclass

    def test_simple_obj(self):
        data_json: str = json.dumps({"name": "John", "age": 30, "city": "New York"})
        data_obj = self.create_obj(data_json)
        self.assertEqual(data_obj.name, "John")
        self.assertEqual(data_obj.age, 30)
        self.assertEqual(data_obj.city, "New York")

    def test_simple_array(self):
        data_json: str = json.dumps(["a", 3, None, True])
        data_obj = self.create_obj(data_json)
        self.assertEqual(data_obj[0], "a")
        self.assertEqual(data_obj[1], 3)
        self.assertEqual(data_obj[2], None)
        self.assertEqual(data_obj[3], True)

    def test_array_of_simple_obj(self):
        data_json: str = json.dumps([{"name": "John"}, {"age": 30}])
        data_obj = self.create_obj(data_json)
        self.assertEqual(data_obj[0].name, "John")
        self.assertEqual(data_obj[1].age, 30)

    def test_obj_with_array(self):
        data_json: str = json.dumps({"name": ["John", "Mark", "Thomas"]})
        data_obj = self.create_obj(data_json)
        self.assertEqual(data_obj.name[0], "John")
        self.assertEqual(data_obj.name[1], "Mark")
        self.assertEqual(data_obj.name[2], "Thomas")

    def test_complex_obj_array(self):
        data_json: str = json.dumps({"a": ["b", {"c": 3}, "e"]})
        data_obj = self.create_obj(data_json)
        self.assertEqual(data_obj.a[0], "b")
        self.assertEqual(data_obj.a[1].c, 3)
        self.assertEqual(data_obj.a[2], "e")

    def test_simple_nested_obj(self):
        data_json: str = json.dumps({"a": {"b": "c", "d": 3}, "e": "f"})
        data_obj = json_to_dataclass(data_json)
        self.assertEqual(data_obj.e, "f")
        self.assertEqual(data_obj.a.b, "c")
        self.assertEqual(data_obj.a.d, 3)

    def test_nested_obj_with_array(self):
        data_json: str = json.dumps({"a": {"b": "c", "d": 3, "g": [1, 2, 3]}, "e": "f"})
        data_obj = json_to_dataclass(data_json)
        self.assertEqual(data_obj.e, "f")
        self.assertEqual(data_obj.a.b, "c")
        self.assertEqual(data_obj.a.g[0], 1)
        self.assertEqual(data_obj.a.g[1], 2)
        self.assertEqual(data_obj.a.g[2], 3)
        self.assertEqual(data_obj.a.d, 3)

    def test_complex_nested_obj_with_array(self):
        data_json: str = json.dumps({"a": ["b", {"c": 3, "f": [1, {"a": "s"}]}, "e"]})
        data_obj = self.create_obj(data_json)
        self.assertEqual(data_obj.a[0], "b")
        self.assertEqual(data_obj.a[1].c, 3)
        self.assertEqual(data_obj.a[2], "e")
        self.assertEqual(data_obj.a[1].f[0], 1)
        self.assertEqual(data_obj.a[1].f[1].a, "s")


if __name__ == "__main__":
    unittest.main()
