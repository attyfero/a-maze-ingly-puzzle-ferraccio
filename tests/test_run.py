import unittest

try:
    # python 3.4+ should use builtin unittest.mock not mock package
    from unittest.mock import patch
except ImportError:
    from mock import patch

import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
pdir = os.path.dirname(currentdir)
ppdir = os.path.dirname(pdir)
sys.path.append(pdir)
sys.path.append(ppdir)

from src.run import Run


class TestRun(unittest.TestCase):
    def setUp(self):
        self.run_class = Run()

    #### check_input_parameter ####

    def test_check_input_parameter_ok(self):
        print("test_check_input_parameter_ok")

        # load sys args in mock
        testargs = ["<programname>", "<json input path>", 2, "Knife,Potted Plant"]
        with patch.object(sys, 'argv', testargs):
            inputparams = sys.argv
            response = self.run_class.check_input_parameter(inputparams)

            self.assertIsNotNone(response)

    def test_check_input_parameter_badnumber(self):
        print("test_check_input_parameter_badnumber")

        # load sys args in mock
        testargs = ["<programname>", "<json input path>", 2]
        with patch.object(sys, 'argv', testargs):
            inputparams = sys.argv
            response = self.run_class.check_input_parameter(inputparams)

            self.assertIsNone(response)

    #### get_file_as_string ####

    def test_get_file_as_string_ok(self):
        response = self.run_class.get_file_as_string("./tests/input_json/json_input_file.json")
        self.assertIsNotNone(response)


    def test_get_file_as_string_ko(self):
        response = self.run_class.get_file_as_string("./tests/input_json/json_input_file_fake.json")
        self.assertIsNone(response)

    def test_get_file_as_string_empty(self):
        response = self.run_class.get_file_as_string("")
        self.assertIsNone(response)

    def test_get_file_as_string_None(self):
        response = self.run_class.get_file_as_string(None)
        self.assertIsNone(response)

    #### get_int_node_id ####

    def test_get_int_node_id_ok(self):
        response = self.run_class.get_int_node_id(2)
        self.assertIsNotNone(response)

    def test_get_int_node_id_ok2(self):
        response = self.run_class.get_int_node_id("2")
        self.assertIsNotNone(response)

    def test_get_int_node_id_badnumber(self):
        response = self.run_class.get_int_node_id("a")
        self.assertIsNone(response)

    #### get_list_from_string ####

    def test_get_list_from_string_ok(self):
        expected_list = ["Pippo", "Pluto"]
        response = self.run_class.get_list_from_string("Pippo,Pluto")
        self.assertListEqual(response, expected_list)
        self.assertEqual(len(response), 2)

    def test_get_list_from_string_ok2(self):
        expected_list = ["Pippo", "Pluto"]
        response = self.run_class.get_list_from_string("    Pippo    ,    Pluto   ")
        self.assertListEqual(response, expected_list)
        self.assertEqual(len(response), 2)

    def test_get_list_from_string_None(self):
        response = self.run_class.get_list_from_string(None)
        self.assertIsNone(response)

    def test_get_list_from_string_Empty(self):
        response = self.run_class.get_list_from_string("")
        self.assertIsNone(response)