# -*- coding: utf-8 -*-
import sys
from pprint import pprint
import traceback
from route_finder import Route_finder

class Run:

    def main(self):
        """Main function to star finder"""

        try:
            inputparams = sys.argv

            if not self.check_input_parameter(inputparams):
                print("Input parameter bad or null")
                sys.exit(0)

            json_file = self.get_file_as_string(inputparams[1])

            root_node = inputparams[2]

            int_root_node = self.get_int_node_id(root_node)

            # check root node
            if not int_root_node:
                print("Input param invalid ")
                sys.exit(0)

            # build word list parameters
            input_word_parameters = self.get_list_from_string(inputparams[3])

            if not input_word_parameters:
                print("Input string list bad or null ")
                sys.exit(0)

            # start searching
            searcher = Route_finder(int(root_node), json_file, input_word_parameters)
            searcher.print_output()

        except:
            print("Some exception happen")
            traceback.print_exc()

    def check_input_parameter(self, inputparams):
        """Verify input parameter"""
        if inputparams and len(inputparams) >= 4:
            return "ok"

    def get_file_as_string(self, input_file_name):
        """Get a file and put it into a variable"""
        if not input_file_name:
            return None

        try:
            # Performe the close file
            with open(input_file_name, 'r') as f:
                json_file = f.read()
        except FileNotFoundError:
            return None

        return json_file

    def get_int_node_id(self, root_node):
        """Transform variable in int if possible"""
        try:
            int_root_node = int(root_node)

            # check root node
            if not int_root_node:
                print('Root node bad or null')
                return None

        except ValueError:
            return None

        return int_root_node

    def get_list_from_string(self, input_string):
        """Get a string with ',' character separator and return a list"""
        if not input_string:
            return None

        # build word list parameters
        input_word_parameters = [x.strip() for x in input_string.split(',')] #input_string.split(",")

        print(input_word_parameters)

        while '' in input_word_parameters:
            input_word_parameters.remove('')

        print("Word params: %s" % input_word_parameters)

        if len(input_word_parameters) <= 0:
            print("Word Input params invalid ")
            return None

        return input_word_parameters

if __name__ == "__main__":
    Run().main()