import os
import sys
import unittest
from pprint import pprint

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
sys.path.append(os.path.abspath(os.path.join(PROJECT_DIR, "src", "cyberyozh_utils")))

from json_serializer import JsonSerializer


class TestJsonSerialize(unittest.TestCase):

    def test_config(self):
        """
        Test reading from Mock config file
        """
        example_json = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "ip_report.json"))
        self.assertTrue(os.path.isfile(example_json))

        json_data = JsonSerializer.deserialize(example_json)
        self.assertIsNotNone(json_data)
        self.assertTrue(isinstance(json_data, dict))
        pprint(json_data)


if __name__ == "__main__":
    unittest.main()
