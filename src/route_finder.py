# -*- coding: utf-8 -*-
import sys
from common import Common
import traceback
from tabulate import tabulate

class Route_finder:
    """Route finder class"""

    def __init__(self, root_node=0, json_file='', input_word_parameters=[]):
        self.common = Common()
        self.root_node = root_node
        self.input_word_parameters = input_word_parameters
        self.output = [['ID', 'Room', 'Object collected']]
        self.json_input_object = self.common.json_validation(json_file)

        # Contain all word found during cicles
        serched_word = []

        # start computation
        self.search_object(self.common.get_item_from_id(self.json_input_object, int(self.root_node)), serched_word)

    def search_object(self, element_obj, serched_word):
        """Search the object inside the list"""
        if not element_obj:
            return None

        words_array = []

        if not len(serched_word) == len(self.input_word_parameters):
            for word_item in self.input_word_parameters:
                try:
                    word_found = [item for item in element_obj['objects'] if item["name"].upper() == word_item.upper()]
                    if word_found and len(word_found) > 0:
                        words_array.append(word_found[0]['name'])
                        serched_word.append(word_found[0]['name'])
                except:
                    print("Error in word for")
                    traceback.print_exc()
                    pass

            if words_array:
                objects_collected = ','.join(words_array)
            else:
                objects_collected = 'None'

            id_item = element_obj["id"]
            name_item = element_obj["name"]

            self.output.append([id_item, name_item, objects_collected])
            self.path_finder(element_obj, serched_word)


    def path_finder(self, element_obj, serched_word):
        """Find the path throw the node connected"""
        position_of_item = [i for i, j in enumerate(self.json_input_object['rooms']) if j == element_obj]

        if 'north' in element_obj:
            new_node = element_obj['north']
            self.json_input_object['rooms'][position_of_item[0]].pop('north')
            self.search_object(self.common.get_item_from_id(self.json_input_object, new_node), serched_word)

        if 'south' in element_obj:
            new_node = element_obj['south']
            self.json_input_object['rooms'][position_of_item[0]].pop('south')
            self.search_object(self.common.get_item_from_id(self.json_input_object, new_node), serched_word)

        if 'west' in element_obj:
            new_node = element_obj['west']
            self.json_input_object['rooms'][position_of_item[0]].pop('west')
            self.search_object(self.common.get_item_from_id(self.json_input_object, new_node), serched_word)

        if 'east' in element_obj:
            new_node = element_obj['east']
            self.json_input_object['rooms'][position_of_item[0]].pop('east')
            self.search_object(self.common.get_item_from_id(self.json_input_object, new_node), serched_word)

    def print_output(self):
        """Print the otput result"""
        print(tabulate(self.output[1:], headers=self.output[0]))