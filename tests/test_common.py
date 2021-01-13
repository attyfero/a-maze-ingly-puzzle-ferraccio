import unittest

#from .context import src
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
pdir = os.path.dirname(currentdir)
ppdir = os.path.dirname(pdir)
sys.path.append(pdir)
sys.path.append(ppdir)

from src.common import Common

class TestCommon(unittest.TestCase):

    def setUp(self):
        self.commonclass = Common()

    ##### json_validation #####

    def test_json_validation_ok(self):
        print("test_json_validation_ok")
        # Load json
        with open("./tests/input_json/json_input_file.json", 'r') as f:
            json_file = f.read()

        # do test
        json_loaded = self.commonclass.json_validation(json_file)
        self.assertIsNotNone(json_loaded)

    def test_json_validation_ko(self):
        print("test_json_validation_ko")
        # Load json
        with open("./tests/input_json/fake_json_input_file.json", 'r') as f:
            json_file = f.read()

        # do test
        json_loaded = self.commonclass.json_validation(json_file)
        self.assertIsNone(json_loaded)

    def test_json_validation_None(self):
        print("test_json_validation_none")
        # Load json
        with open("./tests/input_json/empty_json_input_file.json", 'r') as f:
            json_file = f.read()

        # do test
        json_loaded = self.commonclass.json_validation(json_file)
        self.assertIsNone(json_loaded)


    ##### get_item_from_id #####

    def test_get_item_from_id_ok(self):
        print("test_get_item_from_id_ok")
        # Load json
        with open("./tests/input_json/json_input_file.json", 'r') as f:
            json_file = f.read()
        json_loaded = self.commonclass.json_validation(json_file)

        # do test
        item = self.commonclass.get_item_from_id(json_loaded, 1)
        self.assertIsNotNone(item)

    def test_get_item_from_id_ko(self):
        print("test_get_item_from_id_ko")
        # Load json
        with open("./tests/input_json/json_input_file.json", 'r') as f:
            json_file = f.read()
        json_loaded = self.commonclass.json_validation(json_file)

        # do test
        item = self.commonclass.get_item_from_id(json_loaded, 20)
        self.assertIsNone(item)


if __name__ == '__main__':
    unittest.main()